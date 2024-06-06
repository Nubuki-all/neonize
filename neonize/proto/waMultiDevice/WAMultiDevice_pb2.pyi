"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MultiDevice(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Metadata(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        APPLICATIONDATA_FIELD_NUMBER: builtins.int
        SIGNAL_FIELD_NUMBER: builtins.int
        @property
        def applicationData(self) -> global___MultiDevice.ApplicationData: ...
        @property
        def signal(self) -> global___MultiDevice.Signal: ...
        def __init__(
            self,
            *,
            applicationData: global___MultiDevice.ApplicationData | None = ...,
            signal: global___MultiDevice.Signal | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "applicationData",
                b"applicationData",
                "payload",
                b"payload",
                "signal",
                b"signal",
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "applicationData",
                b"applicationData",
                "payload",
                b"payload",
                "signal",
                b"signal",
            ],
        ) -> None: ...
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["payload", b"payload"]
        ) -> typing_extensions.Literal["applicationData", "signal"] | None: ...

    @typing_extensions.final
    class ApplicationData(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing_extensions.final
        class AppStateSyncKeyRequestMessage(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            KEYIDS_FIELD_NUMBER: builtins.int
            @property
            def keyIDs(
                self,
            ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
                global___MultiDevice.ApplicationData.AppStateSyncKeyId
            ]: ...
            def __init__(
                self,
                *,
                keyIDs: collections.abc.Iterable[
                    global___MultiDevice.ApplicationData.AppStateSyncKeyId
                ]
                | None = ...,
            ) -> None: ...
            def ClearField(
                self, field_name: typing_extensions.Literal["keyIDs", b"keyIDs"]
            ) -> None: ...

        @typing_extensions.final
        class AppStateSyncKeyShareMessage(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            KEYS_FIELD_NUMBER: builtins.int
            @property
            def keys(
                self,
            ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
                global___MultiDevice.ApplicationData.AppStateSyncKey
            ]: ...
            def __init__(
                self,
                *,
                keys: collections.abc.Iterable[
                    global___MultiDevice.ApplicationData.AppStateSyncKey
                ]
                | None = ...,
            ) -> None: ...
            def ClearField(
                self, field_name: typing_extensions.Literal["keys", b"keys"]
            ) -> None: ...

        @typing_extensions.final
        class AppStateSyncKey(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            @typing_extensions.final
            class AppStateSyncKeyData(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                @typing_extensions.final
                class AppStateSyncKeyFingerprint(google.protobuf.message.Message):
                    DESCRIPTOR: google.protobuf.descriptor.Descriptor

                    RAWID_FIELD_NUMBER: builtins.int
                    CURRENTINDEX_FIELD_NUMBER: builtins.int
                    DEVICEINDEXES_FIELD_NUMBER: builtins.int
                    rawID: builtins.int
                    currentIndex: builtins.int
                    @property
                    def deviceIndexes(
                        self,
                    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
                        builtins.int
                    ]: ...
                    def __init__(
                        self,
                        *,
                        rawID: builtins.int | None = ...,
                        currentIndex: builtins.int | None = ...,
                        deviceIndexes: collections.abc.Iterable[builtins.int]
                        | None = ...,
                    ) -> None: ...
                    def HasField(
                        self,
                        field_name: typing_extensions.Literal[
                            "currentIndex", b"currentIndex", "rawID", b"rawID"
                        ],
                    ) -> builtins.bool: ...
                    def ClearField(
                        self,
                        field_name: typing_extensions.Literal[
                            "currentIndex",
                            b"currentIndex",
                            "deviceIndexes",
                            b"deviceIndexes",
                            "rawID",
                            b"rawID",
                        ],
                    ) -> None: ...

                KEYDATA_FIELD_NUMBER: builtins.int
                FINGERPRINT_FIELD_NUMBER: builtins.int
                TIMESTAMP_FIELD_NUMBER: builtins.int
                keyData: builtins.bytes
                @property
                def fingerprint(
                    self,
                ) -> global___MultiDevice.ApplicationData.AppStateSyncKey.AppStateSyncKeyData.AppStateSyncKeyFingerprint: ...
                timestamp: builtins.int
                def __init__(
                    self,
                    *,
                    keyData: builtins.bytes | None = ...,
                    fingerprint: global___MultiDevice.ApplicationData.AppStateSyncKey.AppStateSyncKeyData.AppStateSyncKeyFingerprint
                    | None = ...,
                    timestamp: builtins.int | None = ...,
                ) -> None: ...
                def HasField(
                    self,
                    field_name: typing_extensions.Literal[
                        "fingerprint",
                        b"fingerprint",
                        "keyData",
                        b"keyData",
                        "timestamp",
                        b"timestamp",
                    ],
                ) -> builtins.bool: ...
                def ClearField(
                    self,
                    field_name: typing_extensions.Literal[
                        "fingerprint",
                        b"fingerprint",
                        "keyData",
                        b"keyData",
                        "timestamp",
                        b"timestamp",
                    ],
                ) -> None: ...

            KEYID_FIELD_NUMBER: builtins.int
            KEYDATA_FIELD_NUMBER: builtins.int
            @property
            def keyID(
                self,
            ) -> global___MultiDevice.ApplicationData.AppStateSyncKeyId: ...
            @property
            def keyData(
                self,
            ) -> (
                global___MultiDevice.ApplicationData.AppStateSyncKey.AppStateSyncKeyData
            ): ...
            def __init__(
                self,
                *,
                keyID: global___MultiDevice.ApplicationData.AppStateSyncKeyId
                | None = ...,
                keyData: global___MultiDevice.ApplicationData.AppStateSyncKey.AppStateSyncKeyData
                | None = ...,
            ) -> None: ...
            def HasField(
                self,
                field_name: typing_extensions.Literal[
                    "keyData", b"keyData", "keyID", b"keyID"
                ],
            ) -> builtins.bool: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal[
                    "keyData", b"keyData", "keyID", b"keyID"
                ],
            ) -> None: ...

        @typing_extensions.final
        class AppStateSyncKeyId(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            KEYID_FIELD_NUMBER: builtins.int
            keyID: builtins.bytes
            def __init__(
                self,
                *,
                keyID: builtins.bytes | None = ...,
            ) -> None: ...
            def HasField(
                self, field_name: typing_extensions.Literal["keyID", b"keyID"]
            ) -> builtins.bool: ...
            def ClearField(
                self, field_name: typing_extensions.Literal["keyID", b"keyID"]
            ) -> None: ...

        APPSTATESYNCKEYSHARE_FIELD_NUMBER: builtins.int
        APPSTATESYNCKEYREQUEST_FIELD_NUMBER: builtins.int
        @property
        def appStateSyncKeyShare(
            self,
        ) -> global___MultiDevice.ApplicationData.AppStateSyncKeyShareMessage: ...
        @property
        def appStateSyncKeyRequest(
            self,
        ) -> global___MultiDevice.ApplicationData.AppStateSyncKeyRequestMessage: ...
        def __init__(
            self,
            *,
            appStateSyncKeyShare: global___MultiDevice.ApplicationData.AppStateSyncKeyShareMessage
            | None = ...,
            appStateSyncKeyRequest: global___MultiDevice.ApplicationData.AppStateSyncKeyRequestMessage
            | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "appStateSyncKeyRequest",
                b"appStateSyncKeyRequest",
                "appStateSyncKeyShare",
                b"appStateSyncKeyShare",
                "applicationData",
                b"applicationData",
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "appStateSyncKeyRequest",
                b"appStateSyncKeyRequest",
                "appStateSyncKeyShare",
                b"appStateSyncKeyShare",
                "applicationData",
                b"applicationData",
            ],
        ) -> None: ...
        def WhichOneof(
            self,
            oneof_group: typing_extensions.Literal[
                "applicationData", b"applicationData"
            ],
        ) -> (
            typing_extensions.Literal["appStateSyncKeyShare", "appStateSyncKeyRequest"]
            | None
        ): ...

    @typing_extensions.final
    class Signal(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    PAYLOAD_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    @property
    def payload(self) -> global___MultiDevice.Payload: ...
    @property
    def metadata(self) -> global___MultiDevice.Metadata: ...
    def __init__(
        self,
        *,
        payload: global___MultiDevice.Payload | None = ...,
        metadata: global___MultiDevice.Metadata | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "metadata", b"metadata", "payload", b"payload"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "metadata", b"metadata", "payload", b"payload"
        ],
    ) -> None: ...

global___MultiDevice = MultiDevice
