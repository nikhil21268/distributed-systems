from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyClientRequest(_message.Message):
    __slots__ = ("updated_item",)
    class Item(_message.Message):
        __slots__ = ("id", "price", "name", "category", "description", "quantity_remaining", "seller", "rating")
        ID_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_REMAINING_FIELD_NUMBER: _ClassVar[int]
        SELLER_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        id: int
        price: float
        name: str
        category: str
        description: str
        quantity_remaining: int
        seller: str
        rating: float
        def __init__(self, id: _Optional[int] = ..., price: _Optional[float] = ..., name: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., quantity_remaining: _Optional[int] = ..., seller: _Optional[str] = ..., rating: _Optional[float] = ...) -> None: ...
    UPDATED_ITEM_FIELD_NUMBER: _ClassVar[int]
    updated_item: NotifyClientRequest.Item
    def __init__(self, updated_item: _Optional[_Union[NotifyClientRequest.Item, _Mapping]] = ...) -> None: ...

class NotifyClientResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...
