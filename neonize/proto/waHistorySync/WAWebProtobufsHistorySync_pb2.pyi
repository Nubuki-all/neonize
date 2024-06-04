"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing
import waChatLockSettings.WAProtobufsChatLockSettings_pb2
import waE2E.WAWebProtobufsE2E_pb2
import waSyncAction.WASyncAction_pb2
import waWeb.WAWebProtobufsWeb_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _MediaVisibility:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _MediaVisibilityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MediaVisibility.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DEFAULT: _MediaVisibility.ValueType  # 0
    OFF: _MediaVisibility.ValueType  # 1
    ON: _MediaVisibility.ValueType  # 2

class MediaVisibility(_MediaVisibility, metaclass=_MediaVisibilityEnumTypeWrapper): ...

DEFAULT: MediaVisibility.ValueType  # 0
OFF: MediaVisibility.ValueType  # 1
ON: MediaVisibility.ValueType  # 2
global___MediaVisibility = MediaVisibility

class _PrivacySystemMessage:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PrivacySystemMessageEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PrivacySystemMessage.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    E2EE_MSG: _PrivacySystemMessage.ValueType  # 1
    NE2EE_SELF: _PrivacySystemMessage.ValueType  # 2
    NE2EE_OTHER: _PrivacySystemMessage.ValueType  # 3

class PrivacySystemMessage(_PrivacySystemMessage, metaclass=_PrivacySystemMessageEnumTypeWrapper): ...

E2EE_MSG: PrivacySystemMessage.ValueType  # 1
NE2EE_SELF: PrivacySystemMessage.ValueType  # 2
NE2EE_OTHER: PrivacySystemMessage.ValueType  # 3
global___PrivacySystemMessage = PrivacySystemMessage

@typing_extensions.final
class HistorySync(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _BotAIWaitListState:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _BotAIWaitListStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[HistorySync._BotAIWaitListState.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        IN_WAITLIST: HistorySync._BotAIWaitListState.ValueType  # 0
        AI_AVAILABLE: HistorySync._BotAIWaitListState.ValueType  # 1

    class BotAIWaitListState(_BotAIWaitListState, metaclass=_BotAIWaitListStateEnumTypeWrapper): ...
    IN_WAITLIST: HistorySync.BotAIWaitListState.ValueType  # 0
    AI_AVAILABLE: HistorySync.BotAIWaitListState.ValueType  # 1

    class _HistorySyncType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HistorySyncTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[HistorySync._HistorySyncType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        INITIAL_BOOTSTRAP: HistorySync._HistorySyncType.ValueType  # 0
        INITIAL_STATUS_V3: HistorySync._HistorySyncType.ValueType  # 1
        FULL: HistorySync._HistorySyncType.ValueType  # 2
        RECENT: HistorySync._HistorySyncType.ValueType  # 3
        PUSH_NAME: HistorySync._HistorySyncType.ValueType  # 4
        NON_BLOCKING_DATA: HistorySync._HistorySyncType.ValueType  # 5
        ON_DEMAND: HistorySync._HistorySyncType.ValueType  # 6

    class HistorySyncType(_HistorySyncType, metaclass=_HistorySyncTypeEnumTypeWrapper): ...
    INITIAL_BOOTSTRAP: HistorySync.HistorySyncType.ValueType  # 0
    INITIAL_STATUS_V3: HistorySync.HistorySyncType.ValueType  # 1
    FULL: HistorySync.HistorySyncType.ValueType  # 2
    RECENT: HistorySync.HistorySyncType.ValueType  # 3
    PUSH_NAME: HistorySync.HistorySyncType.ValueType  # 4
    NON_BLOCKING_DATA: HistorySync.HistorySyncType.ValueType  # 5
    ON_DEMAND: HistorySync.HistorySyncType.ValueType  # 6

    SYNCTYPE_FIELD_NUMBER: builtins.int
    CONVERSATIONS_FIELD_NUMBER: builtins.int
    STATUSV3MESSAGES_FIELD_NUMBER: builtins.int
    CHUNKORDER_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    PUSHNAMES_FIELD_NUMBER: builtins.int
    GLOBALSETTINGS_FIELD_NUMBER: builtins.int
    THREADIDUSERSECRET_FIELD_NUMBER: builtins.int
    THREADDSTIMEFRAMEOFFSET_FIELD_NUMBER: builtins.int
    RECENTSTICKERS_FIELD_NUMBER: builtins.int
    PASTPARTICIPANTS_FIELD_NUMBER: builtins.int
    CALLLOGRECORDS_FIELD_NUMBER: builtins.int
    AIWAITLISTSTATE_FIELD_NUMBER: builtins.int
    PHONENUMBERTOLIDMAPPINGS_FIELD_NUMBER: builtins.int
    syncType: global___HistorySync.HistorySyncType.ValueType
    @property
    def conversations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Conversation]: ...
    @property
    def statusV3Messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[waWeb.WAWebProtobufsWeb_pb2.WebMessageInfo]: ...
    chunkOrder: builtins.int
    progress: builtins.int
    @property
    def pushnames(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Pushname]: ...
    @property
    def globalSettings(self) -> global___GlobalSettings: ...
    threadIDUserSecret: builtins.bytes
    threadDsTimeframeOffset: builtins.int
    @property
    def recentStickers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StickerMetadata]: ...
    @property
    def pastParticipants(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PastParticipants]: ...
    @property
    def callLogRecords(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[waSyncAction.WASyncAction_pb2.CallLogRecord]: ...
    aiWaitListState: global___HistorySync.BotAIWaitListState.ValueType
    @property
    def phoneNumberToLidMappings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PhoneNumberToLIDMapping]: ...
    def __init__(
        self,
        *,
        syncType: global___HistorySync.HistorySyncType.ValueType | None = ...,
        conversations: collections.abc.Iterable[global___Conversation] | None = ...,
        statusV3Messages: collections.abc.Iterable[waWeb.WAWebProtobufsWeb_pb2.WebMessageInfo] | None = ...,
        chunkOrder: builtins.int | None = ...,
        progress: builtins.int | None = ...,
        pushnames: collections.abc.Iterable[global___Pushname] | None = ...,
        globalSettings: global___GlobalSettings | None = ...,
        threadIDUserSecret: builtins.bytes | None = ...,
        threadDsTimeframeOffset: builtins.int | None = ...,
        recentStickers: collections.abc.Iterable[global___StickerMetadata] | None = ...,
        pastParticipants: collections.abc.Iterable[global___PastParticipants] | None = ...,
        callLogRecords: collections.abc.Iterable[waSyncAction.WASyncAction_pb2.CallLogRecord] | None = ...,
        aiWaitListState: global___HistorySync.BotAIWaitListState.ValueType | None = ...,
        phoneNumberToLidMappings: collections.abc.Iterable[global___PhoneNumberToLIDMapping] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["aiWaitListState", b"aiWaitListState", "chunkOrder", b"chunkOrder", "globalSettings", b"globalSettings", "progress", b"progress", "syncType", b"syncType", "threadDsTimeframeOffset", b"threadDsTimeframeOffset", "threadIDUserSecret", b"threadIDUserSecret"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["aiWaitListState", b"aiWaitListState", "callLogRecords", b"callLogRecords", "chunkOrder", b"chunkOrder", "conversations", b"conversations", "globalSettings", b"globalSettings", "pastParticipants", b"pastParticipants", "phoneNumberToLidMappings", b"phoneNumberToLidMappings", "progress", b"progress", "pushnames", b"pushnames", "recentStickers", b"recentStickers", "statusV3Messages", b"statusV3Messages", "syncType", b"syncType", "threadDsTimeframeOffset", b"threadDsTimeframeOffset", "threadIDUserSecret", b"threadIDUserSecret"]) -> None: ...

global___HistorySync = HistorySync

@typing_extensions.final
class Conversation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _EndOfHistoryTransferType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EndOfHistoryTransferTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Conversation._EndOfHistoryTransferType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        COMPLETE_BUT_MORE_MESSAGES_REMAIN_ON_PRIMARY: Conversation._EndOfHistoryTransferType.ValueType  # 0
        COMPLETE_AND_NO_MORE_MESSAGE_REMAIN_ON_PRIMARY: Conversation._EndOfHistoryTransferType.ValueType  # 1
        COMPLETE_ON_DEMAND_SYNC_BUT_MORE_MSG_REMAIN_ON_PRIMARY: Conversation._EndOfHistoryTransferType.ValueType  # 2

    class EndOfHistoryTransferType(_EndOfHistoryTransferType, metaclass=_EndOfHistoryTransferTypeEnumTypeWrapper): ...
    COMPLETE_BUT_MORE_MESSAGES_REMAIN_ON_PRIMARY: Conversation.EndOfHistoryTransferType.ValueType  # 0
    COMPLETE_AND_NO_MORE_MESSAGE_REMAIN_ON_PRIMARY: Conversation.EndOfHistoryTransferType.ValueType  # 1
    COMPLETE_ON_DEMAND_SYNC_BUT_MORE_MSG_REMAIN_ON_PRIMARY: Conversation.EndOfHistoryTransferType.ValueType  # 2

    ID_FIELD_NUMBER: builtins.int
    MESSAGES_FIELD_NUMBER: builtins.int
    NEWJID_FIELD_NUMBER: builtins.int
    OLDJID_FIELD_NUMBER: builtins.int
    LASTMSGTIMESTAMP_FIELD_NUMBER: builtins.int
    UNREADCOUNT_FIELD_NUMBER: builtins.int
    READONLY_FIELD_NUMBER: builtins.int
    ENDOFHISTORYTRANSFER_FIELD_NUMBER: builtins.int
    EPHEMERALEXPIRATION_FIELD_NUMBER: builtins.int
    EPHEMERALSETTINGTIMESTAMP_FIELD_NUMBER: builtins.int
    ENDOFHISTORYTRANSFERTYPE_FIELD_NUMBER: builtins.int
    CONVERSATIONTIMESTAMP_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PHASH_FIELD_NUMBER: builtins.int
    NOTSPAM_FIELD_NUMBER: builtins.int
    ARCHIVED_FIELD_NUMBER: builtins.int
    DISAPPEARINGMODE_FIELD_NUMBER: builtins.int
    UNREADMENTIONCOUNT_FIELD_NUMBER: builtins.int
    MARKEDASUNREAD_FIELD_NUMBER: builtins.int
    PARTICIPANT_FIELD_NUMBER: builtins.int
    TCTOKEN_FIELD_NUMBER: builtins.int
    TCTOKENTIMESTAMP_FIELD_NUMBER: builtins.int
    CONTACTPRIMARYIDENTITYKEY_FIELD_NUMBER: builtins.int
    PINNED_FIELD_NUMBER: builtins.int
    MUTEENDTIME_FIELD_NUMBER: builtins.int
    WALLPAPER_FIELD_NUMBER: builtins.int
    MEDIAVISIBILITY_FIELD_NUMBER: builtins.int
    TCTOKENSENDERTIMESTAMP_FIELD_NUMBER: builtins.int
    SUSPENDED_FIELD_NUMBER: builtins.int
    TERMINATED_FIELD_NUMBER: builtins.int
    CREATEDAT_FIELD_NUMBER: builtins.int
    CREATEDBY_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SUPPORT_FIELD_NUMBER: builtins.int
    ISPARENTGROUP_FIELD_NUMBER: builtins.int
    PARENTGROUPID_FIELD_NUMBER: builtins.int
    ISDEFAULTSUBGROUP_FIELD_NUMBER: builtins.int
    DISPLAYNAME_FIELD_NUMBER: builtins.int
    PNJID_FIELD_NUMBER: builtins.int
    SHAREOWNPN_FIELD_NUMBER: builtins.int
    PNHDUPLICATELIDTHREAD_FIELD_NUMBER: builtins.int
    LIDJID_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    LIDORIGINTYPE_FIELD_NUMBER: builtins.int
    COMMENTSCOUNT_FIELD_NUMBER: builtins.int
    LOCKED_FIELD_NUMBER: builtins.int
    SYSTEMMESSAGETOINSERT_FIELD_NUMBER: builtins.int
    ID: builtins.str
    @property
    def messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HistorySyncMsg]: ...
    newJID: builtins.str
    oldJID: builtins.str
    lastMsgTimestamp: builtins.int
    unreadCount: builtins.int
    readOnly: builtins.bool
    endOfHistoryTransfer: builtins.bool
    ephemeralExpiration: builtins.int
    ephemeralSettingTimestamp: builtins.int
    endOfHistoryTransferType: global___Conversation.EndOfHistoryTransferType.ValueType
    conversationTimestamp: builtins.int
    name: builtins.str
    pHash: builtins.str
    notSpam: builtins.bool
    archived: builtins.bool
    @property
    def disappearingMode(self) -> waE2E.WAWebProtobufsE2E_pb2.DisappearingMode: ...
    unreadMentionCount: builtins.int
    markedAsUnread: builtins.bool
    @property
    def participant(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GroupParticipant]: ...
    tcToken: builtins.bytes
    tcTokenTimestamp: builtins.int
    contactPrimaryIdentityKey: builtins.bytes
    pinned: builtins.int
    muteEndTime: builtins.int
    @property
    def wallpaper(self) -> global___WallpaperSettings: ...
    mediaVisibility: global___MediaVisibility.ValueType
    tcTokenSenderTimestamp: builtins.int
    suspended: builtins.bool
    terminated: builtins.bool
    createdAt: builtins.int
    createdBy: builtins.str
    description: builtins.str
    support: builtins.bool
    isParentGroup: builtins.bool
    parentGroupID: builtins.str
    isDefaultSubgroup: builtins.bool
    displayName: builtins.str
    pnJID: builtins.str
    shareOwnPn: builtins.bool
    pnhDuplicateLidThread: builtins.bool
    lidJID: builtins.str
    username: builtins.str
    lidOriginType: builtins.str
    commentsCount: builtins.int
    locked: builtins.bool
    systemMessageToInsert: global___PrivacySystemMessage.ValueType
    def __init__(
        self,
        *,
        ID: builtins.str | None = ...,
        messages: collections.abc.Iterable[global___HistorySyncMsg] | None = ...,
        newJID: builtins.str | None = ...,
        oldJID: builtins.str | None = ...,
        lastMsgTimestamp: builtins.int | None = ...,
        unreadCount: builtins.int | None = ...,
        readOnly: builtins.bool | None = ...,
        endOfHistoryTransfer: builtins.bool | None = ...,
        ephemeralExpiration: builtins.int | None = ...,
        ephemeralSettingTimestamp: builtins.int | None = ...,
        endOfHistoryTransferType: global___Conversation.EndOfHistoryTransferType.ValueType | None = ...,
        conversationTimestamp: builtins.int | None = ...,
        name: builtins.str | None = ...,
        pHash: builtins.str | None = ...,
        notSpam: builtins.bool | None = ...,
        archived: builtins.bool | None = ...,
        disappearingMode: waE2E.WAWebProtobufsE2E_pb2.DisappearingMode | None = ...,
        unreadMentionCount: builtins.int | None = ...,
        markedAsUnread: builtins.bool | None = ...,
        participant: collections.abc.Iterable[global___GroupParticipant] | None = ...,
        tcToken: builtins.bytes | None = ...,
        tcTokenTimestamp: builtins.int | None = ...,
        contactPrimaryIdentityKey: builtins.bytes | None = ...,
        pinned: builtins.int | None = ...,
        muteEndTime: builtins.int | None = ...,
        wallpaper: global___WallpaperSettings | None = ...,
        mediaVisibility: global___MediaVisibility.ValueType | None = ...,
        tcTokenSenderTimestamp: builtins.int | None = ...,
        suspended: builtins.bool | None = ...,
        terminated: builtins.bool | None = ...,
        createdAt: builtins.int | None = ...,
        createdBy: builtins.str | None = ...,
        description: builtins.str | None = ...,
        support: builtins.bool | None = ...,
        isParentGroup: builtins.bool | None = ...,
        parentGroupID: builtins.str | None = ...,
        isDefaultSubgroup: builtins.bool | None = ...,
        displayName: builtins.str | None = ...,
        pnJID: builtins.str | None = ...,
        shareOwnPn: builtins.bool | None = ...,
        pnhDuplicateLidThread: builtins.bool | None = ...,
        lidJID: builtins.str | None = ...,
        username: builtins.str | None = ...,
        lidOriginType: builtins.str | None = ...,
        commentsCount: builtins.int | None = ...,
        locked: builtins.bool | None = ...,
        systemMessageToInsert: global___PrivacySystemMessage.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ID", b"ID", "archived", b"archived", "commentsCount", b"commentsCount", "contactPrimaryIdentityKey", b"contactPrimaryIdentityKey", "conversationTimestamp", b"conversationTimestamp", "createdAt", b"createdAt", "createdBy", b"createdBy", "description", b"description", "disappearingMode", b"disappearingMode", "displayName", b"displayName", "endOfHistoryTransfer", b"endOfHistoryTransfer", "endOfHistoryTransferType", b"endOfHistoryTransferType", "ephemeralExpiration", b"ephemeralExpiration", "ephemeralSettingTimestamp", b"ephemeralSettingTimestamp", "isDefaultSubgroup", b"isDefaultSubgroup", "isParentGroup", b"isParentGroup", "lastMsgTimestamp", b"lastMsgTimestamp", "lidJID", b"lidJID", "lidOriginType", b"lidOriginType", "locked", b"locked", "markedAsUnread", b"markedAsUnread", "mediaVisibility", b"mediaVisibility", "muteEndTime", b"muteEndTime", "name", b"name", "newJID", b"newJID", "notSpam", b"notSpam", "oldJID", b"oldJID", "pHash", b"pHash", "parentGroupID", b"parentGroupID", "pinned", b"pinned", "pnJID", b"pnJID", "pnhDuplicateLidThread", b"pnhDuplicateLidThread", "readOnly", b"readOnly", "shareOwnPn", b"shareOwnPn", "support", b"support", "suspended", b"suspended", "systemMessageToInsert", b"systemMessageToInsert", "tcToken", b"tcToken", "tcTokenSenderTimestamp", b"tcTokenSenderTimestamp", "tcTokenTimestamp", b"tcTokenTimestamp", "terminated", b"terminated", "unreadCount", b"unreadCount", "unreadMentionCount", b"unreadMentionCount", "username", b"username", "wallpaper", b"wallpaper"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ID", b"ID", "archived", b"archived", "commentsCount", b"commentsCount", "contactPrimaryIdentityKey", b"contactPrimaryIdentityKey", "conversationTimestamp", b"conversationTimestamp", "createdAt", b"createdAt", "createdBy", b"createdBy", "description", b"description", "disappearingMode", b"disappearingMode", "displayName", b"displayName", "endOfHistoryTransfer", b"endOfHistoryTransfer", "endOfHistoryTransferType", b"endOfHistoryTransferType", "ephemeralExpiration", b"ephemeralExpiration", "ephemeralSettingTimestamp", b"ephemeralSettingTimestamp", "isDefaultSubgroup", b"isDefaultSubgroup", "isParentGroup", b"isParentGroup", "lastMsgTimestamp", b"lastMsgTimestamp", "lidJID", b"lidJID", "lidOriginType", b"lidOriginType", "locked", b"locked", "markedAsUnread", b"markedAsUnread", "mediaVisibility", b"mediaVisibility", "messages", b"messages", "muteEndTime", b"muteEndTime", "name", b"name", "newJID", b"newJID", "notSpam", b"notSpam", "oldJID", b"oldJID", "pHash", b"pHash", "parentGroupID", b"parentGroupID", "participant", b"participant", "pinned", b"pinned", "pnJID", b"pnJID", "pnhDuplicateLidThread", b"pnhDuplicateLidThread", "readOnly", b"readOnly", "shareOwnPn", b"shareOwnPn", "support", b"support", "suspended", b"suspended", "systemMessageToInsert", b"systemMessageToInsert", "tcToken", b"tcToken", "tcTokenSenderTimestamp", b"tcTokenSenderTimestamp", "tcTokenTimestamp", b"tcTokenTimestamp", "terminated", b"terminated", "unreadCount", b"unreadCount", "unreadMentionCount", b"unreadMentionCount", "username", b"username", "wallpaper", b"wallpaper"]) -> None: ...

global___Conversation = Conversation

@typing_extensions.final
class GroupParticipant(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Rank:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RankEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[GroupParticipant._Rank.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        REGULAR: GroupParticipant._Rank.ValueType  # 0
        ADMIN: GroupParticipant._Rank.ValueType  # 1
        SUPERADMIN: GroupParticipant._Rank.ValueType  # 2

    class Rank(_Rank, metaclass=_RankEnumTypeWrapper): ...
    REGULAR: GroupParticipant.Rank.ValueType  # 0
    ADMIN: GroupParticipant.Rank.ValueType  # 1
    SUPERADMIN: GroupParticipant.Rank.ValueType  # 2

    USERJID_FIELD_NUMBER: builtins.int
    RANK_FIELD_NUMBER: builtins.int
    userJID: builtins.str
    rank: global___GroupParticipant.Rank.ValueType
    def __init__(
        self,
        *,
        userJID: builtins.str | None = ...,
        rank: global___GroupParticipant.Rank.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["rank", b"rank", "userJID", b"userJID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["rank", b"rank", "userJID", b"userJID"]) -> None: ...

global___GroupParticipant = GroupParticipant

@typing_extensions.final
class PastParticipant(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _LeaveReason:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _LeaveReasonEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PastParticipant._LeaveReason.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        LEFT: PastParticipant._LeaveReason.ValueType  # 0
        REMOVED: PastParticipant._LeaveReason.ValueType  # 1

    class LeaveReason(_LeaveReason, metaclass=_LeaveReasonEnumTypeWrapper): ...
    LEFT: PastParticipant.LeaveReason.ValueType  # 0
    REMOVED: PastParticipant.LeaveReason.ValueType  # 1

    USERJID_FIELD_NUMBER: builtins.int
    LEAVEREASON_FIELD_NUMBER: builtins.int
    LEAVETS_FIELD_NUMBER: builtins.int
    userJID: builtins.str
    leaveReason: global___PastParticipant.LeaveReason.ValueType
    leaveTS: builtins.int
    def __init__(
        self,
        *,
        userJID: builtins.str | None = ...,
        leaveReason: global___PastParticipant.LeaveReason.ValueType | None = ...,
        leaveTS: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["leaveReason", b"leaveReason", "leaveTS", b"leaveTS", "userJID", b"userJID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["leaveReason", b"leaveReason", "leaveTS", b"leaveTS", "userJID", b"userJID"]) -> None: ...

global___PastParticipant = PastParticipant

@typing_extensions.final
class PhoneNumberToLIDMapping(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PNJID_FIELD_NUMBER: builtins.int
    LIDJID_FIELD_NUMBER: builtins.int
    pnJID: builtins.str
    lidJID: builtins.str
    def __init__(
        self,
        *,
        pnJID: builtins.str | None = ...,
        lidJID: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["lidJID", b"lidJID", "pnJID", b"pnJID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["lidJID", b"lidJID", "pnJID", b"pnJID"]) -> None: ...

global___PhoneNumberToLIDMapping = PhoneNumberToLIDMapping

@typing_extensions.final
class HistorySyncMsg(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGE_FIELD_NUMBER: builtins.int
    MSGORDERID_FIELD_NUMBER: builtins.int
    @property
    def message(self) -> waWeb.WAWebProtobufsWeb_pb2.WebMessageInfo: ...
    msgOrderID: builtins.int
    def __init__(
        self,
        *,
        message: waWeb.WAWebProtobufsWeb_pb2.WebMessageInfo | None = ...,
        msgOrderID: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["message", b"message", "msgOrderID", b"msgOrderID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["message", b"message", "msgOrderID", b"msgOrderID"]) -> None: ...

global___HistorySyncMsg = HistorySyncMsg

@typing_extensions.final
class Pushname(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    PUSHNAME_FIELD_NUMBER: builtins.int
    ID: builtins.str
    pushname: builtins.str
    def __init__(
        self,
        *,
        ID: builtins.str | None = ...,
        pushname: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ID", b"ID", "pushname", b"pushname"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ID", b"ID", "pushname", b"pushname"]) -> None: ...

global___Pushname = Pushname

@typing_extensions.final
class WallpaperSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILENAME_FIELD_NUMBER: builtins.int
    OPACITY_FIELD_NUMBER: builtins.int
    filename: builtins.str
    opacity: builtins.int
    def __init__(
        self,
        *,
        filename: builtins.str | None = ...,
        opacity: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filename", b"filename", "opacity", b"opacity"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filename", b"filename", "opacity", b"opacity"]) -> None: ...

global___WallpaperSettings = WallpaperSettings

@typing_extensions.final
class GlobalSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIGHTTHEMEWALLPAPER_FIELD_NUMBER: builtins.int
    MEDIAVISIBILITY_FIELD_NUMBER: builtins.int
    DARKTHEMEWALLPAPER_FIELD_NUMBER: builtins.int
    AUTODOWNLOADWIFI_FIELD_NUMBER: builtins.int
    AUTODOWNLOADCELLULAR_FIELD_NUMBER: builtins.int
    AUTODOWNLOADROAMING_FIELD_NUMBER: builtins.int
    SHOWINDIVIDUALNOTIFICATIONSPREVIEW_FIELD_NUMBER: builtins.int
    SHOWGROUPNOTIFICATIONSPREVIEW_FIELD_NUMBER: builtins.int
    DISAPPEARINGMODEDURATION_FIELD_NUMBER: builtins.int
    DISAPPEARINGMODETIMESTAMP_FIELD_NUMBER: builtins.int
    AVATARUSERSETTINGS_FIELD_NUMBER: builtins.int
    FONTSIZE_FIELD_NUMBER: builtins.int
    SECURITYNOTIFICATIONS_FIELD_NUMBER: builtins.int
    AUTOUNARCHIVECHATS_FIELD_NUMBER: builtins.int
    VIDEOQUALITYMODE_FIELD_NUMBER: builtins.int
    PHOTOQUALITYMODE_FIELD_NUMBER: builtins.int
    INDIVIDUALNOTIFICATIONSETTINGS_FIELD_NUMBER: builtins.int
    GROUPNOTIFICATIONSETTINGS_FIELD_NUMBER: builtins.int
    CHATLOCKSETTINGS_FIELD_NUMBER: builtins.int
    @property
    def lightThemeWallpaper(self) -> global___WallpaperSettings: ...
    mediaVisibility: global___MediaVisibility.ValueType
    @property
    def darkThemeWallpaper(self) -> global___WallpaperSettings: ...
    @property
    def autoDownloadWiFi(self) -> global___AutoDownloadSettings: ...
    @property
    def autoDownloadCellular(self) -> global___AutoDownloadSettings: ...
    @property
    def autoDownloadRoaming(self) -> global___AutoDownloadSettings: ...
    showIndividualNotificationsPreview: builtins.bool
    showGroupNotificationsPreview: builtins.bool
    disappearingModeDuration: builtins.int
    disappearingModeTimestamp: builtins.int
    @property
    def avatarUserSettings(self) -> global___AvatarUserSettings: ...
    fontSize: builtins.int
    securityNotifications: builtins.bool
    autoUnarchiveChats: builtins.bool
    videoQualityMode: builtins.int
    photoQualityMode: builtins.int
    @property
    def individualNotificationSettings(self) -> global___NotificationSettings: ...
    @property
    def groupNotificationSettings(self) -> global___NotificationSettings: ...
    @property
    def chatLockSettings(self) -> waChatLockSettings.WAProtobufsChatLockSettings_pb2.ChatLockSettings: ...
    def __init__(
        self,
        *,
        lightThemeWallpaper: global___WallpaperSettings | None = ...,
        mediaVisibility: global___MediaVisibility.ValueType | None = ...,
        darkThemeWallpaper: global___WallpaperSettings | None = ...,
        autoDownloadWiFi: global___AutoDownloadSettings | None = ...,
        autoDownloadCellular: global___AutoDownloadSettings | None = ...,
        autoDownloadRoaming: global___AutoDownloadSettings | None = ...,
        showIndividualNotificationsPreview: builtins.bool | None = ...,
        showGroupNotificationsPreview: builtins.bool | None = ...,
        disappearingModeDuration: builtins.int | None = ...,
        disappearingModeTimestamp: builtins.int | None = ...,
        avatarUserSettings: global___AvatarUserSettings | None = ...,
        fontSize: builtins.int | None = ...,
        securityNotifications: builtins.bool | None = ...,
        autoUnarchiveChats: builtins.bool | None = ...,
        videoQualityMode: builtins.int | None = ...,
        photoQualityMode: builtins.int | None = ...,
        individualNotificationSettings: global___NotificationSettings | None = ...,
        groupNotificationSettings: global___NotificationSettings | None = ...,
        chatLockSettings: waChatLockSettings.WAProtobufsChatLockSettings_pb2.ChatLockSettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["autoDownloadCellular", b"autoDownloadCellular", "autoDownloadRoaming", b"autoDownloadRoaming", "autoDownloadWiFi", b"autoDownloadWiFi", "autoUnarchiveChats", b"autoUnarchiveChats", "avatarUserSettings", b"avatarUserSettings", "chatLockSettings", b"chatLockSettings", "darkThemeWallpaper", b"darkThemeWallpaper", "disappearingModeDuration", b"disappearingModeDuration", "disappearingModeTimestamp", b"disappearingModeTimestamp", "fontSize", b"fontSize", "groupNotificationSettings", b"groupNotificationSettings", "individualNotificationSettings", b"individualNotificationSettings", "lightThemeWallpaper", b"lightThemeWallpaper", "mediaVisibility", b"mediaVisibility", "photoQualityMode", b"photoQualityMode", "securityNotifications", b"securityNotifications", "showGroupNotificationsPreview", b"showGroupNotificationsPreview", "showIndividualNotificationsPreview", b"showIndividualNotificationsPreview", "videoQualityMode", b"videoQualityMode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["autoDownloadCellular", b"autoDownloadCellular", "autoDownloadRoaming", b"autoDownloadRoaming", "autoDownloadWiFi", b"autoDownloadWiFi", "autoUnarchiveChats", b"autoUnarchiveChats", "avatarUserSettings", b"avatarUserSettings", "chatLockSettings", b"chatLockSettings", "darkThemeWallpaper", b"darkThemeWallpaper", "disappearingModeDuration", b"disappearingModeDuration", "disappearingModeTimestamp", b"disappearingModeTimestamp", "fontSize", b"fontSize", "groupNotificationSettings", b"groupNotificationSettings", "individualNotificationSettings", b"individualNotificationSettings", "lightThemeWallpaper", b"lightThemeWallpaper", "mediaVisibility", b"mediaVisibility", "photoQualityMode", b"photoQualityMode", "securityNotifications", b"securityNotifications", "showGroupNotificationsPreview", b"showGroupNotificationsPreview", "showIndividualNotificationsPreview", b"showIndividualNotificationsPreview", "videoQualityMode", b"videoQualityMode"]) -> None: ...

global___GlobalSettings = GlobalSettings

@typing_extensions.final
class AutoDownloadSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOWNLOADIMAGES_FIELD_NUMBER: builtins.int
    DOWNLOADAUDIO_FIELD_NUMBER: builtins.int
    DOWNLOADVIDEO_FIELD_NUMBER: builtins.int
    DOWNLOADDOCUMENTS_FIELD_NUMBER: builtins.int
    downloadImages: builtins.bool
    downloadAudio: builtins.bool
    downloadVideo: builtins.bool
    downloadDocuments: builtins.bool
    def __init__(
        self,
        *,
        downloadImages: builtins.bool | None = ...,
        downloadAudio: builtins.bool | None = ...,
        downloadVideo: builtins.bool | None = ...,
        downloadDocuments: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["downloadAudio", b"downloadAudio", "downloadDocuments", b"downloadDocuments", "downloadImages", b"downloadImages", "downloadVideo", b"downloadVideo"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["downloadAudio", b"downloadAudio", "downloadDocuments", b"downloadDocuments", "downloadImages", b"downloadImages", "downloadVideo", b"downloadVideo"]) -> None: ...

global___AutoDownloadSettings = AutoDownloadSettings

@typing_extensions.final
class StickerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    FILESHA256_FIELD_NUMBER: builtins.int
    FILEENCSHA256_FIELD_NUMBER: builtins.int
    MEDIAKEY_FIELD_NUMBER: builtins.int
    MIMETYPE_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    DIRECTPATH_FIELD_NUMBER: builtins.int
    FILELENGTH_FIELD_NUMBER: builtins.int
    WEIGHT_FIELD_NUMBER: builtins.int
    LASTSTICKERSENTTS_FIELD_NUMBER: builtins.int
    ISLOTTIE_FIELD_NUMBER: builtins.int
    URL: builtins.str
    fileSHA256: builtins.bytes
    fileEncSHA256: builtins.bytes
    mediaKey: builtins.bytes
    mimetype: builtins.str
    height: builtins.int
    width: builtins.int
    directPath: builtins.str
    fileLength: builtins.int
    weight: builtins.float
    lastStickerSentTS: builtins.int
    isLottie: builtins.bool
    def __init__(
        self,
        *,
        URL: builtins.str | None = ...,
        fileSHA256: builtins.bytes | None = ...,
        fileEncSHA256: builtins.bytes | None = ...,
        mediaKey: builtins.bytes | None = ...,
        mimetype: builtins.str | None = ...,
        height: builtins.int | None = ...,
        width: builtins.int | None = ...,
        directPath: builtins.str | None = ...,
        fileLength: builtins.int | None = ...,
        weight: builtins.float | None = ...,
        lastStickerSentTS: builtins.int | None = ...,
        isLottie: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["URL", b"URL", "directPath", b"directPath", "fileEncSHA256", b"fileEncSHA256", "fileLength", b"fileLength", "fileSHA256", b"fileSHA256", "height", b"height", "isLottie", b"isLottie", "lastStickerSentTS", b"lastStickerSentTS", "mediaKey", b"mediaKey", "mimetype", b"mimetype", "weight", b"weight", "width", b"width"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["URL", b"URL", "directPath", b"directPath", "fileEncSHA256", b"fileEncSHA256", "fileLength", b"fileLength", "fileSHA256", b"fileSHA256", "height", b"height", "isLottie", b"isLottie", "lastStickerSentTS", b"lastStickerSentTS", "mediaKey", b"mediaKey", "mimetype", b"mimetype", "weight", b"weight", "width", b"width"]) -> None: ...

global___StickerMetadata = StickerMetadata

@typing_extensions.final
class PastParticipants(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GROUPJID_FIELD_NUMBER: builtins.int
    PASTPARTICIPANTS_FIELD_NUMBER: builtins.int
    groupJID: builtins.str
    @property
    def pastParticipants(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PastParticipant]: ...
    def __init__(
        self,
        *,
        groupJID: builtins.str | None = ...,
        pastParticipants: collections.abc.Iterable[global___PastParticipant] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["groupJID", b"groupJID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["groupJID", b"groupJID", "pastParticipants", b"pastParticipants"]) -> None: ...

global___PastParticipants = PastParticipants

@typing_extensions.final
class AvatarUserSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FBID_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    FBID: builtins.str
    password: builtins.str
    def __init__(
        self,
        *,
        FBID: builtins.str | None = ...,
        password: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["FBID", b"FBID", "password", b"password"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["FBID", b"FBID", "password", b"password"]) -> None: ...

global___AvatarUserSettings = AvatarUserSettings

@typing_extensions.final
class NotificationSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGEVIBRATE_FIELD_NUMBER: builtins.int
    MESSAGEPOPUP_FIELD_NUMBER: builtins.int
    MESSAGELIGHT_FIELD_NUMBER: builtins.int
    LOWPRIORITYNOTIFICATIONS_FIELD_NUMBER: builtins.int
    REACTIONSMUTED_FIELD_NUMBER: builtins.int
    CALLVIBRATE_FIELD_NUMBER: builtins.int
    messageVibrate: builtins.str
    messagePopup: builtins.str
    messageLight: builtins.str
    lowPriorityNotifications: builtins.bool
    reactionsMuted: builtins.bool
    callVibrate: builtins.str
    def __init__(
        self,
        *,
        messageVibrate: builtins.str | None = ...,
        messagePopup: builtins.str | None = ...,
        messageLight: builtins.str | None = ...,
        lowPriorityNotifications: builtins.bool | None = ...,
        reactionsMuted: builtins.bool | None = ...,
        callVibrate: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["callVibrate", b"callVibrate", "lowPriorityNotifications", b"lowPriorityNotifications", "messageLight", b"messageLight", "messagePopup", b"messagePopup", "messageVibrate", b"messageVibrate", "reactionsMuted", b"reactionsMuted"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["callVibrate", b"callVibrate", "lowPriorityNotifications", b"lowPriorityNotifications", "messageLight", b"messageLight", "messagePopup", b"messagePopup", "messageVibrate", b"messageVibrate", "reactionsMuted", b"reactionsMuted"]) -> None: ...

global___NotificationSettings = NotificationSettings
