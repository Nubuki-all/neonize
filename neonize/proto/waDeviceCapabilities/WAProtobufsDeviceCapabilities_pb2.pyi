"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class DeviceCapabilities(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ChatLockSupportLevel:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ChatLockSupportLevelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeviceCapabilities._ChatLockSupportLevel.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NONE: DeviceCapabilities._ChatLockSupportLevel.ValueType  # 0
        MINIMAL: DeviceCapabilities._ChatLockSupportLevel.ValueType  # 1
        FULL: DeviceCapabilities._ChatLockSupportLevel.ValueType  # 2

    class ChatLockSupportLevel(_ChatLockSupportLevel, metaclass=_ChatLockSupportLevelEnumTypeWrapper): ...
    NONE: DeviceCapabilities.ChatLockSupportLevel.ValueType  # 0
    MINIMAL: DeviceCapabilities.ChatLockSupportLevel.ValueType  # 1
    FULL: DeviceCapabilities.ChatLockSupportLevel.ValueType  # 2

    CHATLOCKSUPPORTLEVEL_FIELD_NUMBER: builtins.int
    chatLockSupportLevel: global___DeviceCapabilities.ChatLockSupportLevel.ValueType
    def __init__(
        self,
        *,
        chatLockSupportLevel: global___DeviceCapabilities.ChatLockSupportLevel.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["chatLockSupportLevel", b"chatLockSupportLevel"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["chatLockSupportLevel", b"chatLockSupportLevel"]) -> None: ...

global___DeviceCapabilities = DeviceCapabilities
