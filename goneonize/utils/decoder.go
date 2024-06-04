package utils

import (
	"time"

	"github.com/krypton-byte/neonize/defproto"
	"go.mau.fi/whatsmeow"
	"go.mau.fi/whatsmeow/appstate"
	waVname "go.mau.fi/whatsmeow/proto/waVnameCert"
	"go.mau.fi/whatsmeow/store"
	"go.mau.fi/whatsmeow/types"
)

func DecodeJidProto(data *defproto.JID) types.JID {
	return types.JID{
		User:       *data.User,
		RawAgent:   uint8(*data.RawAgent),
		Device:     uint16(*data.Device),
		Integrator: uint16(*data.Integrator),
		Server:     *data.Server,
	}
}

func DecodeGroupParent(groupParent *defproto.GroupParent) types.GroupParent {
	return types.GroupParent{
		IsParent:                      *groupParent.IsParent,
		DefaultMembershipApprovalMode: *groupParent.DefaultMembershipApprovalMode,
	}
}

func DecodeGroupLinkedParent(groupLinkedParent *defproto.GroupLinkedParent) types.GroupLinkedParent {
	return types.GroupLinkedParent{
		LinkedParentJID: DecodeJidProto(groupLinkedParent.LinkedParentJID),
	}
}

func DecodeReqCreateGroup(reqCreateGroup *defproto.ReqCreateGroup) whatsmeow.ReqCreateGroup {
	participants := []types.JID{}
	for _, participant := range reqCreateGroup.Participants {
		participants = append(participants, DecodeJidProto(participant))
	}
	new_type := whatsmeow.ReqCreateGroup{
		Name:         *reqCreateGroup.Name,
		Participants: participants,
		CreateKey:    *reqCreateGroup.CreateKey,
	}
	if reqCreateGroup.GroupParent != nil {
		new_type.GroupParent = DecodeGroupParent(reqCreateGroup.GroupParent)
	}
	if reqCreateGroup.GroupLinkedParent != nil {
		new_type.GroupLinkedParent = DecodeGroupLinkedParent(reqCreateGroup.GroupLinkedParent)
	}
	return new_type
}
func DecodeMessageSource(messageSource *defproto.MessageSource) types.MessageSource {
	return types.MessageSource{
		Chat:               DecodeJidProto(messageSource.Chat),
		Sender:             DecodeJidProto(messageSource.Sender),
		IsFromMe:           *messageSource.IsFromMe,
		IsGroup:            *messageSource.IsGroup,
		BroadcastListOwner: DecodeJidProto(messageSource.BroadcastListOwner),
	}
}
func DecodeVerifiedNameCertificate(verifiedNameCertificate *waVname.VerifiedNameCertificate) *waVname.VerifiedNameCertificate {
	//passing types through protobuf
	return verifiedNameCertificate

}

func DecodeVerifiedNameDetails(verifiedNameDetails *waVname.VerifiedNameCertificate_Details) *waVname.VerifiedNameCertificate_Details {
	return verifiedNameDetails
}
func DecodeVerifiedName(verifiedName *defproto.VerifiedName) *types.VerifiedName {
	verifiednametypes := types.VerifiedName{}
	if verifiedName.Certificate != nil {
		verifiednametypes.Certificate = verifiednametypes.Certificate
	}
	if verifiedName.Details != nil {
		verifiednametypes.Details = verifiednametypes.Details
	}
	return &verifiednametypes
}
func DecodeDeviceSentMeta(deviceSentMeta *defproto.DeviceSentMeta) *types.DeviceSentMeta {
	return &types.DeviceSentMeta{
		DestinationJID: *deviceSentMeta.DestinationJID,
		Phash:          *deviceSentMeta.Phash,
	}
}
func DecodeMessageInfo(messageInfo *defproto.MessageInfo) *types.MessageInfo {
	ts := *messageInfo.Timestamp
	model := &types.MessageInfo{
		MessageSource: DecodeMessageSource(messageInfo.MessageSource),
		ID:            *messageInfo.ID,
		ServerID:      int(*messageInfo.ServerID),
		Type:          *messageInfo.Type,
		PushName:      *messageInfo.Pushname,
		Timestamp:     time.Unix(0, ts),
		Category:      *messageInfo.Category,
		Multicast:     *messageInfo.Multicast,
		MediaType:     *messageInfo.MediaType,
		Edit:          types.EditAttribute(*messageInfo.Edit),
	}
	if messageInfo.VerifiedName != nil {
		model.VerifiedName = DecodeVerifiedName(messageInfo.VerifiedName)
	}
	if messageInfo.DeviceSentMeta != nil {
		model.DeviceSentMeta = DecodeDeviceSentMeta(messageInfo.DeviceSentMeta)
	}
	return model
}

func DecodeCreateNewsletterParams(createletterNewsParams *defproto.CreateNewsletterParams) whatsmeow.CreateNewsletterParams {
	return whatsmeow.CreateNewsletterParams{
		Name:        *createletterNewsParams.Name,
		Description: *createletterNewsParams.Description,
		Picture:     createletterNewsParams.Picture,
	}
}

func DecodeGetProfilePictureParams(params *defproto.GetProfilePictureParams) *whatsmeow.GetProfilePictureParams {
	if params.Preview == nil || params.ExistingID == nil || params.IsCommunity == nil {
		return nil
	}
	return &whatsmeow.GetProfilePictureParams{
		Preview:     *params.Preview,
		ExistingID:  *params.ExistingID,
		IsCommunity: *params.IsCommunity,
	}
}
func DecodeMutationInfo(mutationInfo *defproto.MutationInfo) appstate.MutationInfo {
	return appstate.MutationInfo{
		Index:   mutationInfo.Index,
		Version: *mutationInfo.Version,
		Value:   mutationInfo.Value,
	}
}
func DecodePatchInfo(patchInfo *defproto.PatchInfo) *appstate.PatchInfo {
	var Type appstate.WAPatchName
	switch patchInfo.Type {
	case defproto.PatchInfo_CRITICAL_BLOCK.Enum():
		Type = appstate.WAPatchCriticalBlock
	case defproto.PatchInfo_CRITICAL_UNBLOCK_LOW.Enum():
		Type = appstate.WAPatchCriticalUnblockLow
	case defproto.PatchInfo_REGULAR.Enum():
		Type = appstate.WAPatchRegular
	}
	mutationInfo := []appstate.MutationInfo{}
	for _, mutation := range patchInfo.Mutations {
		mutationInfo = append(mutationInfo, DecodeMutationInfo(mutation))
	}
	return &appstate.PatchInfo{
		Timestamp: time.Unix(0, *patchInfo.Timestamp),
		Type:      Type,
		Mutations: mutationInfo,
	}
}

func DecodeContactEntry(entry *defproto.ContactEntry) *store.ContactEntry {
	return &store.ContactEntry{
		JID:       DecodeJidProto(entry.JID),
		FirstName: *entry.FirstName,
		FullName:  *entry.FullName,
	}
}
