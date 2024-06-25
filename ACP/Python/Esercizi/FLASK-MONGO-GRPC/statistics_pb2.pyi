from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Sensor(_message.Message):
    __slots__ = ("id", "dataTipe")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATATIPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    dataTipe: str
    def __init__(self, id: _Optional[str] = ..., dataTipe: _Optional[str] = ...) -> None: ...

class MeanRequest(_message.Message):
    __slots__ = ("id", "dataTipe")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATATIPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    dataTipe: str
    def __init__(self, id: _Optional[str] = ..., dataTipe: _Optional[str] = ...) -> None: ...

class StringMessage(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
