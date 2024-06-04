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

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ADVEncryptionType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ADVEncryptionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ADVEncryptionType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    E2EE: _ADVEncryptionType.ValueType  # 0
    HOSTED: _ADVEncryptionType.ValueType  # 1

class ADVEncryptionType(_ADVEncryptionType, metaclass=_ADVEncryptionTypeEnumTypeWrapper): ...

E2EE: ADVEncryptionType.ValueType  # 0
HOSTED: ADVEncryptionType.ValueType  # 1
global___ADVEncryptionType = ADVEncryptionType

@typing_extensions.final
class ADVKeyIndexList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RAWID_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    CURRENTINDEX_FIELD_NUMBER: builtins.int
    VALIDINDEXES_FIELD_NUMBER: builtins.int
    ACCOUNTTYPE_FIELD_NUMBER: builtins.int
    rawID: builtins.int
    timestamp: builtins.int
    currentIndex: builtins.int
    @property
    def validIndexes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    accountType: global___ADVEncryptionType.ValueType
    def __init__(
        self,
        *,
        rawID: builtins.int | None = ...,
        timestamp: builtins.int | None = ...,
        currentIndex: builtins.int | None = ...,
        validIndexes: collections.abc.Iterable[builtins.int] | None = ...,
        accountType: global___ADVEncryptionType.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["accountType", b"accountType", "currentIndex", b"currentIndex", "rawID", b"rawID", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accountType", b"accountType", "currentIndex", b"currentIndex", "rawID", b"rawID", "timestamp", b"timestamp", "validIndexes", b"validIndexes"]) -> None: ...

global___ADVKeyIndexList = ADVKeyIndexList

@typing_extensions.final
class ADVSignedKeyIndexList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DETAILS_FIELD_NUMBER: builtins.int
    ACCOUNTSIGNATURE_FIELD_NUMBER: builtins.int
    ACCOUNTSIGNATUREKEY_FIELD_NUMBER: builtins.int
    details: builtins.bytes
    accountSignature: builtins.bytes
    accountSignatureKey: builtins.bytes
    def __init__(
        self,
        *,
        details: builtins.bytes | None = ...,
        accountSignature: builtins.bytes | None = ...,
        accountSignatureKey: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["accountSignature", b"accountSignature", "accountSignatureKey", b"accountSignatureKey", "details", b"details"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accountSignature", b"accountSignature", "accountSignatureKey", b"accountSignatureKey", "details", b"details"]) -> None: ...

global___ADVSignedKeyIndexList = ADVSignedKeyIndexList

@typing_extensions.final
class ADVDeviceIdentity(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RAWID_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    KEYINDEX_FIELD_NUMBER: builtins.int
    ACCOUNTTYPE_FIELD_NUMBER: builtins.int
    DEVICETYPE_FIELD_NUMBER: builtins.int
    rawID: builtins.int
    timestamp: builtins.int
    keyIndex: builtins.int
    accountType: global___ADVEncryptionType.ValueType
    deviceType: global___ADVEncryptionType.ValueType
    def __init__(
        self,
        *,
        rawID: builtins.int | None = ...,
        timestamp: builtins.int | None = ...,
        keyIndex: builtins.int | None = ...,
        accountType: global___ADVEncryptionType.ValueType | None = ...,
        deviceType: global___ADVEncryptionType.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["accountType", b"accountType", "deviceType", b"deviceType", "keyIndex", b"keyIndex", "rawID", b"rawID", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accountType", b"accountType", "deviceType", b"deviceType", "keyIndex", b"keyIndex", "rawID", b"rawID", "timestamp", b"timestamp"]) -> None: ...

global___ADVDeviceIdentity = ADVDeviceIdentity

@typing_extensions.final
class ADVSignedDeviceIdentity(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DETAILS_FIELD_NUMBER: builtins.int
    ACCOUNTSIGNATUREKEY_FIELD_NUMBER: builtins.int
    ACCOUNTSIGNATURE_FIELD_NUMBER: builtins.int
    DEVICESIGNATURE_FIELD_NUMBER: builtins.int
    details: builtins.bytes
    accountSignatureKey: builtins.bytes
    accountSignature: builtins.bytes
    deviceSignature: builtins.bytes
    def __init__(
        self,
        *,
        details: builtins.bytes | None = ...,
        accountSignatureKey: builtins.bytes | None = ...,
        accountSignature: builtins.bytes | None = ...,
        deviceSignature: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["accountSignature", b"accountSignature", "accountSignatureKey", b"accountSignatureKey", "details", b"details", "deviceSignature", b"deviceSignature"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accountSignature", b"accountSignature", "accountSignatureKey", b"accountSignatureKey", "details", b"details", "deviceSignature", b"deviceSignature"]) -> None: ...

global___ADVSignedDeviceIdentity = ADVSignedDeviceIdentity

@typing_extensions.final
class ADVSignedDeviceIdentityHMAC(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DETAILS_FIELD_NUMBER: builtins.int
    HMAC_FIELD_NUMBER: builtins.int
    ACCOUNTTYPE_FIELD_NUMBER: builtins.int
    details: builtins.bytes
    HMAC: builtins.bytes
    accountType: global___ADVEncryptionType.ValueType
    def __init__(
        self,
        *,
        details: builtins.bytes | None = ...,
        HMAC: builtins.bytes | None = ...,
        accountType: global___ADVEncryptionType.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["HMAC", b"HMAC", "accountType", b"accountType", "details", b"details"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["HMAC", b"HMAC", "accountType", b"accountType", "details", b"details"]) -> None: ...

global___ADVSignedDeviceIdentityHMAC = ADVSignedDeviceIdentityHMAC
