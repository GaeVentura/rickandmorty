from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StringMessage(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class Prodotto(_message.Message):
    __slots__ = ("id", "tipoProdotto")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPOPRODOTTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    tipoProdotto: str
    def __init__(self, id: _Optional[str] = ..., tipoProdotto: _Optional[str] = ...) -> None: ...
