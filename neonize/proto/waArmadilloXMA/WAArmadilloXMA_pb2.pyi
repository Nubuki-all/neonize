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
import waCommon.WACommon_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ExtendedContentMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _OverlayIconGlyph:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _OverlayIconGlyphEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            ExtendedContentMessage._OverlayIconGlyph.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        INFO: ExtendedContentMessage._OverlayIconGlyph.ValueType  # 0
        EYE_OFF: ExtendedContentMessage._OverlayIconGlyph.ValueType  # 1
        NEWS_OFF: ExtendedContentMessage._OverlayIconGlyph.ValueType  # 2
        WARNING: ExtendedContentMessage._OverlayIconGlyph.ValueType  # 3
        PRIVATE: ExtendedContentMessage._OverlayIconGlyph.ValueType  # 4
        NONE: ExtendedContentMessage._OverlayIconGlyph.ValueType  # 5
        MEDIA_LABEL: ExtendedContentMessage._OverlayIconGlyph.ValueType  # 6
        POST_COVER: ExtendedContentMessage._OverlayIconGlyph.ValueType  # 7
        POST_LABEL: ExtendedContentMessage._OverlayIconGlyph.ValueType  # 8
        WARNING_SCREENS: ExtendedContentMessage._OverlayIconGlyph.ValueType  # 9

    class OverlayIconGlyph(
        _OverlayIconGlyph, metaclass=_OverlayIconGlyphEnumTypeWrapper
    ): ...
    INFO: ExtendedContentMessage.OverlayIconGlyph.ValueType  # 0
    EYE_OFF: ExtendedContentMessage.OverlayIconGlyph.ValueType  # 1
    NEWS_OFF: ExtendedContentMessage.OverlayIconGlyph.ValueType  # 2
    WARNING: ExtendedContentMessage.OverlayIconGlyph.ValueType  # 3
    PRIVATE: ExtendedContentMessage.OverlayIconGlyph.ValueType  # 4
    NONE: ExtendedContentMessage.OverlayIconGlyph.ValueType  # 5
    MEDIA_LABEL: ExtendedContentMessage.OverlayIconGlyph.ValueType  # 6
    POST_COVER: ExtendedContentMessage.OverlayIconGlyph.ValueType  # 7
    POST_LABEL: ExtendedContentMessage.OverlayIconGlyph.ValueType  # 8
    WARNING_SCREENS: ExtendedContentMessage.OverlayIconGlyph.ValueType  # 9

    class _CtaButtonType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CtaButtonTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            ExtendedContentMessage._CtaButtonType.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        OPEN_NATIVE: ExtendedContentMessage._CtaButtonType.ValueType  # 11

    class CtaButtonType(_CtaButtonType, metaclass=_CtaButtonTypeEnumTypeWrapper): ...
    OPEN_NATIVE: ExtendedContentMessage.CtaButtonType.ValueType  # 11

    class _XmaLayoutType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _XmaLayoutTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            ExtendedContentMessage._XmaLayoutType.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SINGLE: ExtendedContentMessage._XmaLayoutType.ValueType  # 0
        HSCROLL: ExtendedContentMessage._XmaLayoutType.ValueType  # 1
        PORTRAIT: ExtendedContentMessage._XmaLayoutType.ValueType  # 3
        STANDARD_DXMA: ExtendedContentMessage._XmaLayoutType.ValueType  # 12
        LIST_DXMA: ExtendedContentMessage._XmaLayoutType.ValueType  # 15
        GRID: ExtendedContentMessage._XmaLayoutType.ValueType  # 16

    class XmaLayoutType(_XmaLayoutType, metaclass=_XmaLayoutTypeEnumTypeWrapper): ...
    SINGLE: ExtendedContentMessage.XmaLayoutType.ValueType  # 0
    HSCROLL: ExtendedContentMessage.XmaLayoutType.ValueType  # 1
    PORTRAIT: ExtendedContentMessage.XmaLayoutType.ValueType  # 3
    STANDARD_DXMA: ExtendedContentMessage.XmaLayoutType.ValueType  # 12
    LIST_DXMA: ExtendedContentMessage.XmaLayoutType.ValueType  # 15
    GRID: ExtendedContentMessage.XmaLayoutType.ValueType  # 16

    class _ExtendedContentType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ExtendedContentTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            ExtendedContentMessage._ExtendedContentType.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        IG_STORY_PHOTO_MENTION: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 4
        IG_SINGLE_IMAGE_POST_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 9
        IG_MULTIPOST_SHARE: ExtendedContentMessage._ExtendedContentType.ValueType  # 10
        IG_SINGLE_VIDEO_POST_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 11
        IG_STORY_PHOTO_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 12
        IG_STORY_VIDEO_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 13
        IG_CLIPS_SHARE: ExtendedContentMessage._ExtendedContentType.ValueType  # 14
        IG_IGTV_SHARE: ExtendedContentMessage._ExtendedContentType.ValueType  # 15
        IG_SHOP_SHARE: ExtendedContentMessage._ExtendedContentType.ValueType  # 16
        IG_PROFILE_SHARE: ExtendedContentMessage._ExtendedContentType.ValueType  # 19
        IG_STORY_PHOTO_HIGHLIGHT_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 20
        IG_STORY_VIDEO_HIGHLIGHT_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 21
        IG_STORY_REPLY: ExtendedContentMessage._ExtendedContentType.ValueType  # 22
        IG_STORY_REACTION: ExtendedContentMessage._ExtendedContentType.ValueType  # 23
        IG_STORY_VIDEO_MENTION: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 24
        IG_STORY_HIGHLIGHT_REPLY: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 25
        IG_STORY_HIGHLIGHT_REACTION: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 26
        IG_EXTERNAL_LINK: ExtendedContentMessage._ExtendedContentType.ValueType  # 27
        IG_RECEIVER_FETCH: ExtendedContentMessage._ExtendedContentType.ValueType  # 28
        FB_FEED_SHARE: ExtendedContentMessage._ExtendedContentType.ValueType  # 1000
        FB_STORY_REPLY: ExtendedContentMessage._ExtendedContentType.ValueType  # 1001
        FB_STORY_SHARE: ExtendedContentMessage._ExtendedContentType.ValueType  # 1002
        FB_STORY_MENTION: ExtendedContentMessage._ExtendedContentType.ValueType  # 1003
        FB_FEED_VIDEO_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 1004
        FB_GAMING_CUSTOM_UPDATE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 1005
        FB_PRODUCER_STORY_REPLY: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 1006
        FB_EVENT: ExtendedContentMessage._ExtendedContentType.ValueType  # 1007
        FB_FEED_POST_PRIVATE_REPLY: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 1008
        FB_SHORT: ExtendedContentMessage._ExtendedContentType.ValueType  # 1009
        FB_COMMENT_MENTION_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 1010
        MSG_EXTERNAL_LINK_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2000
        MSG_P2P_PAYMENT: ExtendedContentMessage._ExtendedContentType.ValueType  # 2001
        MSG_LOCATION_SHARING: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2002
        MSG_LOCATION_SHARING_V2: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2003
        MSG_HIGHLIGHTS_TAB_FRIEND_UPDATES_REPLY: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2004
        MSG_HIGHLIGHTS_TAB_LOCAL_EVENT_REPLY: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2005
        MSG_RECEIVER_FETCH: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2006
        MSG_IG_MEDIA_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2007
        MSG_GEN_AI_SEARCH_PLUGIN_RESPONSE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2008
        MSG_REELS_LIST: ExtendedContentMessage._ExtendedContentType.ValueType  # 2009
        MSG_CONTACT: ExtendedContentMessage._ExtendedContentType.ValueType  # 2010
        MSG_THREADS_POST_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2011
        MSG_FILE: ExtendedContentMessage._ExtendedContentType.ValueType  # 2012
        MSG_AVATAR_DETAILS: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2013
        MSG_AI_CONTACT: ExtendedContentMessage._ExtendedContentType.ValueType  # 2014
        MSG_MEMORIES_SHARE: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2015
        MSG_SHARED_ALBUM_REPLY: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 2016
        RTC_AUDIO_CALL: ExtendedContentMessage._ExtendedContentType.ValueType  # 3000
        RTC_VIDEO_CALL: ExtendedContentMessage._ExtendedContentType.ValueType  # 3001
        RTC_MISSED_AUDIO_CALL: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 3002
        RTC_MISSED_VIDEO_CALL: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 3003
        RTC_GROUP_AUDIO_CALL: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 3004
        RTC_GROUP_VIDEO_CALL: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 3005
        RTC_MISSED_GROUP_AUDIO_CALL: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 3006
        RTC_MISSED_GROUP_VIDEO_CALL: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 3007
        DATACLASS_SENDER_COPY: (
            ExtendedContentMessage._ExtendedContentType.ValueType
        )  # 4000

    class ExtendedContentType(
        _ExtendedContentType, metaclass=_ExtendedContentTypeEnumTypeWrapper
    ): ...
    IG_STORY_PHOTO_MENTION: ExtendedContentMessage.ExtendedContentType.ValueType  # 4
    IG_SINGLE_IMAGE_POST_SHARE: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 9
    IG_MULTIPOST_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 10
    IG_SINGLE_VIDEO_POST_SHARE: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 11
    IG_STORY_PHOTO_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 12
    IG_STORY_VIDEO_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 13
    IG_CLIPS_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 14
    IG_IGTV_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 15
    IG_SHOP_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 16
    IG_PROFILE_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 19
    IG_STORY_PHOTO_HIGHLIGHT_SHARE: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 20
    IG_STORY_VIDEO_HIGHLIGHT_SHARE: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 21
    IG_STORY_REPLY: ExtendedContentMessage.ExtendedContentType.ValueType  # 22
    IG_STORY_REACTION: ExtendedContentMessage.ExtendedContentType.ValueType  # 23
    IG_STORY_VIDEO_MENTION: ExtendedContentMessage.ExtendedContentType.ValueType  # 24
    IG_STORY_HIGHLIGHT_REPLY: ExtendedContentMessage.ExtendedContentType.ValueType  # 25
    IG_STORY_HIGHLIGHT_REACTION: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 26
    IG_EXTERNAL_LINK: ExtendedContentMessage.ExtendedContentType.ValueType  # 27
    IG_RECEIVER_FETCH: ExtendedContentMessage.ExtendedContentType.ValueType  # 28
    FB_FEED_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 1000
    FB_STORY_REPLY: ExtendedContentMessage.ExtendedContentType.ValueType  # 1001
    FB_STORY_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 1002
    FB_STORY_MENTION: ExtendedContentMessage.ExtendedContentType.ValueType  # 1003
    FB_FEED_VIDEO_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 1004
    FB_GAMING_CUSTOM_UPDATE: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 1005
    FB_PRODUCER_STORY_REPLY: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 1006
    FB_EVENT: ExtendedContentMessage.ExtendedContentType.ValueType  # 1007
    FB_FEED_POST_PRIVATE_REPLY: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 1008
    FB_SHORT: ExtendedContentMessage.ExtendedContentType.ValueType  # 1009
    FB_COMMENT_MENTION_SHARE: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 1010
    MSG_EXTERNAL_LINK_SHARE: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 2000
    MSG_P2P_PAYMENT: ExtendedContentMessage.ExtendedContentType.ValueType  # 2001
    MSG_LOCATION_SHARING: ExtendedContentMessage.ExtendedContentType.ValueType  # 2002
    MSG_LOCATION_SHARING_V2: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 2003
    MSG_HIGHLIGHTS_TAB_FRIEND_UPDATES_REPLY: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 2004
    MSG_HIGHLIGHTS_TAB_LOCAL_EVENT_REPLY: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 2005
    MSG_RECEIVER_FETCH: ExtendedContentMessage.ExtendedContentType.ValueType  # 2006
    MSG_IG_MEDIA_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 2007
    MSG_GEN_AI_SEARCH_PLUGIN_RESPONSE: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 2008
    MSG_REELS_LIST: ExtendedContentMessage.ExtendedContentType.ValueType  # 2009
    MSG_CONTACT: ExtendedContentMessage.ExtendedContentType.ValueType  # 2010
    MSG_THREADS_POST_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 2011
    MSG_FILE: ExtendedContentMessage.ExtendedContentType.ValueType  # 2012
    MSG_AVATAR_DETAILS: ExtendedContentMessage.ExtendedContentType.ValueType  # 2013
    MSG_AI_CONTACT: ExtendedContentMessage.ExtendedContentType.ValueType  # 2014
    MSG_MEMORIES_SHARE: ExtendedContentMessage.ExtendedContentType.ValueType  # 2015
    MSG_SHARED_ALBUM_REPLY: ExtendedContentMessage.ExtendedContentType.ValueType  # 2016
    RTC_AUDIO_CALL: ExtendedContentMessage.ExtendedContentType.ValueType  # 3000
    RTC_VIDEO_CALL: ExtendedContentMessage.ExtendedContentType.ValueType  # 3001
    RTC_MISSED_AUDIO_CALL: ExtendedContentMessage.ExtendedContentType.ValueType  # 3002
    RTC_MISSED_VIDEO_CALL: ExtendedContentMessage.ExtendedContentType.ValueType  # 3003
    RTC_GROUP_AUDIO_CALL: ExtendedContentMessage.ExtendedContentType.ValueType  # 3004
    RTC_GROUP_VIDEO_CALL: ExtendedContentMessage.ExtendedContentType.ValueType  # 3005
    RTC_MISSED_GROUP_AUDIO_CALL: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 3006
    RTC_MISSED_GROUP_VIDEO_CALL: (
        ExtendedContentMessage.ExtendedContentType.ValueType
    )  # 3007
    DATACLASS_SENDER_COPY: ExtendedContentMessage.ExtendedContentType.ValueType  # 4000

    @typing_extensions.final
    class CTA(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        BUTTONTYPE_FIELD_NUMBER: builtins.int
        TITLE_FIELD_NUMBER: builtins.int
        ACTIONURL_FIELD_NUMBER: builtins.int
        NATIVEURL_FIELD_NUMBER: builtins.int
        CTATYPE_FIELD_NUMBER: builtins.int
        ACTIONCONTENTBLOB_FIELD_NUMBER: builtins.int
        buttonType: global___ExtendedContentMessage.CtaButtonType.ValueType
        title: builtins.str
        actionURL: builtins.str
        nativeURL: builtins.str
        ctaType: builtins.str
        actionContentBlob: builtins.str
        def __init__(
            self,
            *,
            buttonType: global___ExtendedContentMessage.CtaButtonType.ValueType
            | None = ...,
            title: builtins.str | None = ...,
            actionURL: builtins.str | None = ...,
            nativeURL: builtins.str | None = ...,
            ctaType: builtins.str | None = ...,
            actionContentBlob: builtins.str | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "actionContentBlob",
                b"actionContentBlob",
                "actionURL",
                b"actionURL",
                "buttonType",
                b"buttonType",
                "ctaType",
                b"ctaType",
                "nativeURL",
                b"nativeURL",
                "title",
                b"title",
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "actionContentBlob",
                b"actionContentBlob",
                "actionURL",
                b"actionURL",
                "buttonType",
                b"buttonType",
                "ctaType",
                b"ctaType",
                "nativeURL",
                b"nativeURL",
                "title",
                b"title",
            ],
        ) -> None: ...

    ASSOCIATEDMESSAGE_FIELD_NUMBER: builtins.int
    TARGETTYPE_FIELD_NUMBER: builtins.int
    TARGETUSERNAME_FIELD_NUMBER: builtins.int
    TARGETID_FIELD_NUMBER: builtins.int
    TARGETEXPIRINGATSEC_FIELD_NUMBER: builtins.int
    XMALAYOUTTYPE_FIELD_NUMBER: builtins.int
    CTAS_FIELD_NUMBER: builtins.int
    PREVIEWS_FIELD_NUMBER: builtins.int
    TITLETEXT_FIELD_NUMBER: builtins.int
    SUBTITLETEXT_FIELD_NUMBER: builtins.int
    MAXTITLENUMOFLINES_FIELD_NUMBER: builtins.int
    MAXSUBTITLENUMOFLINES_FIELD_NUMBER: builtins.int
    FAVICON_FIELD_NUMBER: builtins.int
    HEADERIMAGE_FIELD_NUMBER: builtins.int
    HEADERTITLE_FIELD_NUMBER: builtins.int
    OVERLAYICONGLYPH_FIELD_NUMBER: builtins.int
    OVERLAYTITLE_FIELD_NUMBER: builtins.int
    OVERLAYDESCRIPTION_FIELD_NUMBER: builtins.int
    SENTWITHMESSAGEID_FIELD_NUMBER: builtins.int
    MESSAGETEXT_FIELD_NUMBER: builtins.int
    HEADERSUBTITLE_FIELD_NUMBER: builtins.int
    XMADATACLASS_FIELD_NUMBER: builtins.int
    CONTENTREF_FIELD_NUMBER: builtins.int
    @property
    def associatedMessage(self) -> waCommon.WACommon_pb2.SubProtocol: ...
    targetType: global___ExtendedContentMessage.ExtendedContentType.ValueType
    targetUsername: builtins.str
    targetID: builtins.str
    targetExpiringAtSec: builtins.int
    xmaLayoutType: global___ExtendedContentMessage.XmaLayoutType.ValueType
    @property
    def ctas(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ExtendedContentMessage.CTA
    ]: ...
    @property
    def previews(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        waCommon.WACommon_pb2.SubProtocol
    ]: ...
    titleText: builtins.str
    subtitleText: builtins.str
    maxTitleNumOfLines: builtins.int
    maxSubtitleNumOfLines: builtins.int
    @property
    def favicon(self) -> waCommon.WACommon_pb2.SubProtocol: ...
    @property
    def headerImage(self) -> waCommon.WACommon_pb2.SubProtocol: ...
    headerTitle: builtins.str
    overlayIconGlyph: global___ExtendedContentMessage.OverlayIconGlyph.ValueType
    overlayTitle: builtins.str
    overlayDescription: builtins.str
    sentWithMessageID: builtins.str
    messageText: builtins.str
    headerSubtitle: builtins.str
    xmaDataclass: builtins.str
    contentRef: builtins.str
    def __init__(
        self,
        *,
        associatedMessage: waCommon.WACommon_pb2.SubProtocol | None = ...,
        targetType: global___ExtendedContentMessage.ExtendedContentType.ValueType
        | None = ...,
        targetUsername: builtins.str | None = ...,
        targetID: builtins.str | None = ...,
        targetExpiringAtSec: builtins.int | None = ...,
        xmaLayoutType: global___ExtendedContentMessage.XmaLayoutType.ValueType
        | None = ...,
        ctas: collections.abc.Iterable[global___ExtendedContentMessage.CTA]
        | None = ...,
        previews: collections.abc.Iterable[waCommon.WACommon_pb2.SubProtocol]
        | None = ...,
        titleText: builtins.str | None = ...,
        subtitleText: builtins.str | None = ...,
        maxTitleNumOfLines: builtins.int | None = ...,
        maxSubtitleNumOfLines: builtins.int | None = ...,
        favicon: waCommon.WACommon_pb2.SubProtocol | None = ...,
        headerImage: waCommon.WACommon_pb2.SubProtocol | None = ...,
        headerTitle: builtins.str | None = ...,
        overlayIconGlyph: global___ExtendedContentMessage.OverlayIconGlyph.ValueType
        | None = ...,
        overlayTitle: builtins.str | None = ...,
        overlayDescription: builtins.str | None = ...,
        sentWithMessageID: builtins.str | None = ...,
        messageText: builtins.str | None = ...,
        headerSubtitle: builtins.str | None = ...,
        xmaDataclass: builtins.str | None = ...,
        contentRef: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "associatedMessage",
            b"associatedMessage",
            "contentRef",
            b"contentRef",
            "favicon",
            b"favicon",
            "headerImage",
            b"headerImage",
            "headerSubtitle",
            b"headerSubtitle",
            "headerTitle",
            b"headerTitle",
            "maxSubtitleNumOfLines",
            b"maxSubtitleNumOfLines",
            "maxTitleNumOfLines",
            b"maxTitleNumOfLines",
            "messageText",
            b"messageText",
            "overlayDescription",
            b"overlayDescription",
            "overlayIconGlyph",
            b"overlayIconGlyph",
            "overlayTitle",
            b"overlayTitle",
            "sentWithMessageID",
            b"sentWithMessageID",
            "subtitleText",
            b"subtitleText",
            "targetExpiringAtSec",
            b"targetExpiringAtSec",
            "targetID",
            b"targetID",
            "targetType",
            b"targetType",
            "targetUsername",
            b"targetUsername",
            "titleText",
            b"titleText",
            "xmaDataclass",
            b"xmaDataclass",
            "xmaLayoutType",
            b"xmaLayoutType",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "associatedMessage",
            b"associatedMessage",
            "contentRef",
            b"contentRef",
            "ctas",
            b"ctas",
            "favicon",
            b"favicon",
            "headerImage",
            b"headerImage",
            "headerSubtitle",
            b"headerSubtitle",
            "headerTitle",
            b"headerTitle",
            "maxSubtitleNumOfLines",
            b"maxSubtitleNumOfLines",
            "maxTitleNumOfLines",
            b"maxTitleNumOfLines",
            "messageText",
            b"messageText",
            "overlayDescription",
            b"overlayDescription",
            "overlayIconGlyph",
            b"overlayIconGlyph",
            "overlayTitle",
            b"overlayTitle",
            "previews",
            b"previews",
            "sentWithMessageID",
            b"sentWithMessageID",
            "subtitleText",
            b"subtitleText",
            "targetExpiringAtSec",
            b"targetExpiringAtSec",
            "targetID",
            b"targetID",
            "targetType",
            b"targetType",
            "targetUsername",
            b"targetUsername",
            "titleText",
            b"titleText",
            "xmaDataclass",
            b"xmaDataclass",
            "xmaLayoutType",
            b"xmaLayoutType",
        ],
    ) -> None: ...

global___ExtendedContentMessage = ExtendedContentMessage
