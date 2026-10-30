package main

/*
   #include <stdlib.h>
*/
import "C"

import (
	"context"
	"encoding/json"
	"errors"
	"io"
	"os/exec"
	"sync"
	"time"

	"github.com/purpshell/meowcaller"
	"go.mau.fi/whatsmeow"
)

// Voice calls through meowcaller. Calls are opt-in per client: EnableCalls must
// run before Neonize connects the client, because meowcaller has to hook the
// <call> node handlers before the receive loop starts.

var (
	callsMu      sync.Mutex
	callsEnabled = map[string]bool{}
	callClients  = map[string]*meowcaller.Client{}
	activeCalls  = map[string]*callEntry{}
)

type callEntry struct {
	owner  string
	call   *meowcaller.Call
	player *meowcaller.Player
}

// installCalls wraps a freshly created whatsmeow client when calls were enabled
// for its uuid. Called from Neonize before the client connects.
func installCalls(uuid string, client *whatsmeow.Client) {
	callsMu.Lock()
	defer callsMu.Unlock()
	if !callsEnabled[uuid] {
		return
	}
	mc := meowcaller.NewClient(client)
	mc.OnIncomingCall(func(call *meowcaller.Call) {
		callsMu.Lock()
		activeCalls[call.ID()] = &callEntry{owner: uuid, call: call}
		callsMu.Unlock()
	})
	callClients[uuid] = mc
}

// removeCalls hangs up a stopped client's calls and forgets its call client.
func removeCalls(uuid string) {
	callsMu.Lock()
	var owned []*callEntry
	for callID, entry := range activeCalls {
		if entry.owner == uuid {
			owned = append(owned, entry)
			delete(activeCalls, callID)
		}
	}
	delete(callClients, uuid)
	delete(callsEnabled, uuid)
	callsMu.Unlock()
	for _, entry := range owned {
		if entry.player != nil {
			entry.player.Stop()
		}
		_ = entry.call.Hangup()
	}
}

type callResult struct {
	CallID string `json:"call_id,omitempty"`
	Error  string `json:"error,omitempty"`
}

func callJSON(v any) *C.char {
	out, err := json.Marshal(v)
	if err != nil {
		return C.CString(`{"error":"` + err.Error() + `"}`)
	}
	return C.CString(string(out))
}

func errString(err error) *C.char {
	if err != nil {
		return C.CString(err.Error())
	}
	return C.CString("")
}

func callClient(id *C.char) (*meowcaller.Client, error) {
	callsMu.Lock()
	defer callsMu.Unlock()
	mc := callClients[C.GoString(id)]
	if mc == nil {
		return nil, errors.New("calls are not enabled for this client (pass enable_calls=True)")
	}
	return mc, nil
}

func getCall(callID *C.char) (*callEntry, error) {
	callsMu.Lock()
	defer callsMu.Unlock()
	entry := activeCalls[C.GoString(callID)]
	if entry == nil {
		return nil, errors.New("unknown call id")
	}
	return entry, nil
}

func registerCall(owner string, call *meowcaller.Call, err error) *C.char {
	if err != nil {
		return callJSON(callResult{Error: err.Error()})
	}
	callsMu.Lock()
	activeCalls[call.ID()] = &callEntry{owner: owner, call: call}
	callsMu.Unlock()
	return callJSON(callResult{CallID: call.ID()})
}

//export EnableCalls
func EnableCalls(id *C.char) {
	callsMu.Lock()
	callsEnabled[C.GoString(id)] = true
	callsMu.Unlock()
}

//export CallUser
func CallUser(id *C.char, target *C.char) *C.char {
	mc, err := callClient(id)
	if err != nil {
		return callJSON(callResult{Error: err.Error()})
	}
	ctx, cancel := context.WithTimeout(context.Background(), 60*time.Second)
	defer cancel()
	call, err := mc.Call(ctx, C.GoString(target))
	return registerCall(C.GoString(id), call, err)
}

//export CallGroup
func CallGroup(id *C.char, groupJID *C.char) *C.char {
	mc, err := callClient(id)
	if err != nil {
		return callJSON(callResult{Error: err.Error()})
	}
	ctx, cancel := context.WithTimeout(context.Background(), 60*time.Second)
	defer cancel()
	call, err := mc.GroupCallByID(ctx, C.GoString(groupJID))
	return registerCall(C.GoString(id), call, err)
}

//export CallAnswer
func CallAnswer(callID *C.char) *C.char {
	entry, err := getCall(callID)
	if err != nil {
		return errString(err)
	}
	return errString(entry.call.Answer())
}

//export CallReject
func CallReject(callID *C.char) *C.char {
	entry, err := getCall(callID)
	if err != nil {
		return errString(err)
	}
	err = entry.call.Reject()
	callsMu.Lock()
	delete(activeCalls, C.GoString(callID))
	callsMu.Unlock()
	return errString(err)
}

//export CallHangup
func CallHangup(callID *C.char) *C.char {
	entry, err := getCall(callID)
	if err != nil {
		return errString(err)
	}
	if entry.player != nil {
		entry.player.Stop()
	}
	err = entry.call.Hangup()
	callsMu.Lock()
	delete(activeCalls, C.GoString(callID))
	callsMu.Unlock()
	return errString(err)
}

// ffmpegPCM decodes any input ffmpeg understands (file path or URL) to the
// 16 kHz mono s16le PCM that meowcaller.PCMStream expects. Closing it stops
// ffmpeg.
type ffmpegPCM struct {
	io.ReadCloser
	cmd *exec.Cmd
}

func (f *ffmpegPCM) Close() error {
	err := f.ReadCloser.Close()
	if f.cmd.Process != nil {
		_ = f.cmd.Process.Kill()
	}
	_ = f.cmd.Wait()
	return err
}

func startFFmpegPCM(source string) (*ffmpegPCM, error) {
	cmd := exec.Command(
		"ffmpeg", "-nostdin", "-loglevel", "error",
		"-i", source,
		"-f", "s16le", "-ac", "1", "-ar", "16000", "pipe:1",
	)
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		return nil, err
	}
	if err := cmd.Start(); err != nil {
		return nil, err
	}
	return &ffmpegPCM{ReadCloser: stdout, cmd: cmd}, nil
}

//export CallPlay
func CallPlay(callID *C.char, source *C.char) *C.char {
	entry, err := getCall(callID)
	if err != nil {
		return errString(err)
	}
	pcm, err := startFFmpegPCM(C.GoString(source))
	if err != nil {
		return errString(err)
	}
	callsMu.Lock()
	if entry.player == nil {
		entry.player = meowcaller.NewPlayer()
		entry.call.Subscribe(entry.player)
	}
	player := entry.player
	callsMu.Unlock()
	player.Play(meowcaller.PCMStream(pcm))
	return errString(nil)
}

func withPlayer(callID *C.char, fn func(*meowcaller.Player)) *C.char {
	entry, err := getCall(callID)
	if err != nil {
		return errString(err)
	}
	callsMu.Lock()
	player := entry.player
	callsMu.Unlock()
	if player == nil {
		return errString(errors.New("nothing is playing in this call"))
	}
	fn(player)
	return errString(nil)
}

//export CallPause
func CallPause(callID *C.char) *C.char {
	return withPlayer(callID, (*meowcaller.Player).Pause)
}

//export CallResume
func CallResume(callID *C.char) *C.char {
	return withPlayer(callID, (*meowcaller.Player).Resume)
}

//export CallStopPlayback
func CallStopPlayback(callID *C.char) *C.char {
	return withPlayer(callID, (*meowcaller.Player).Stop)
}

var callPhaseNames = map[meowcaller.CallPhase]string{
	meowcaller.CallPhaseIdle:        "idle",
	meowcaller.CallPhaseCalling:     "calling",
	meowcaller.CallPhaseRinging:     "ringing",
	meowcaller.CallPhaseConnecting:  "connecting",
	meowcaller.CallPhaseActive:      "active",
	meowcaller.CallPhaseEnded:       "ended",
	meowcaller.CallPhaseWaitingRoom: "waiting_room",
}

var playerStateNames = map[meowcaller.PlayerState]string{
	meowcaller.PlayerIdle:    "idle",
	meowcaller.PlayerPlaying: "playing",
	meowcaller.PlayerPaused:  "paused",
}

type callStateResult struct {
	CallID string `json:"call_id,omitempty"`
	Peer   string `json:"peer,omitempty"`
	State  string `json:"state,omitempty"`
	Player string `json:"player,omitempty"`
	Error  string `json:"error,omitempty"`
}

//export CallState
func CallState(callID *C.char) *C.char {
	entry, err := getCall(callID)
	if err != nil {
		return callJSON(callStateResult{Error: err.Error()})
	}
	callsMu.Lock()
	player := entry.player
	callsMu.Unlock()
	res := callStateResult{
		CallID: entry.call.ID(),
		Peer:   entry.call.Peer().String(),
		State:  callPhaseNames[entry.call.State()],
		Player: "idle",
	}
	if player != nil {
		res.Player = playerStateNames[player.State()]
	}
	return callJSON(res)
}
