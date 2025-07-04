"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import waSyncAction.WASyncAction_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SyncdSnapshotRecovery(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    COLLECTIONNAME_FIELD_NUMBER: builtins.int
    MUTATIONRECORDS_FIELD_NUMBER: builtins.int
    COLLECTIONLTHASH_FIELD_NUMBER: builtins.int
    collectionName: builtins.str
    collectionLthash: builtins.bytes
    @property
    def version(self) -> global___SyncdVersion: ...
    @property
    def mutationRecords(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SyncdPlainTextRecord]: ...
    def __init__(
        self,
        *,
        version: global___SyncdVersion | None = ...,
        collectionName: builtins.str | None = ...,
        mutationRecords: collections.abc.Iterable[global___SyncdPlainTextRecord] | None = ...,
        collectionLthash: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["collectionLthash", b"collectionLthash", "collectionName", b"collectionName", "version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["collectionLthash", b"collectionLthash", "collectionName", b"collectionName", "mutationRecords", b"mutationRecords", "version", b"version"]) -> None: ...

global___SyncdSnapshotRecovery = SyncdSnapshotRecovery

@typing.final
class SyncdPlainTextRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    KEYID_FIELD_NUMBER: builtins.int
    MAC_FIELD_NUMBER: builtins.int
    keyID: builtins.bytes
    mac: builtins.bytes
    @property
    def value(self) -> waSyncAction.WASyncAction_pb2.SyncActionData: ...
    def __init__(
        self,
        *,
        value: waSyncAction.WASyncAction_pb2.SyncActionData | None = ...,
        keyID: builtins.bytes | None = ...,
        mac: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["keyID", b"keyID", "mac", b"mac", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["keyID", b"keyID", "mac", b"mac", "value", b"value"]) -> None: ...

global___SyncdPlainTextRecord = SyncdPlainTextRecord

@typing.final
class SyncdVersion(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    version: builtins.int
    def __init__(
        self,
        *,
        version: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["version", b"version"]) -> None: ...

global___SyncdVersion = SyncdVersion
