"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import waUserPassword.WAProtobufsUserPassword_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ChatLockSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HIDELOCKEDCHATS_FIELD_NUMBER: builtins.int
    SECRETCODE_FIELD_NUMBER: builtins.int
    hideLockedChats: builtins.bool
    @property
    def secretCode(self) -> waUserPassword.WAProtobufsUserPassword_pb2.UserPassword: ...
    def __init__(
        self,
        *,
        hideLockedChats: builtins.bool | None = ...,
        secretCode: waUserPassword.WAProtobufsUserPassword_pb2.UserPassword
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "hideLockedChats", b"hideLockedChats", "secretCode", b"secretCode"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "hideLockedChats", b"hideLockedChats", "secretCode", b"secretCode"
        ],
    ) -> None: ...

global___ChatLockSettings = ChatLockSettings
