from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchItemRequest(_message.Message):
    __slots__ = ("item_name", "category")
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    item_name: str
    category: str
    def __init__(self, item_name: _Optional[str] = ..., category: _Optional[str] = ...) -> None: ...

class SearchItemResponse(_message.Message):
    __slots__ = ("items",)
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
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SearchItemResponse.Item]
    def __init__(self, items: _Optional[_Iterable[_Union[SearchItemResponse.Item, _Mapping]]] = ...) -> None: ...

class BuyItemRequest(_message.Message):
    __slots__ = ("item_id", "quantity", "buyer_address")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    BUYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    quantity: int
    buyer_address: str
    def __init__(self, item_id: _Optional[int] = ..., quantity: _Optional[int] = ..., buyer_address: _Optional[str] = ...) -> None: ...

class BuyItemResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class AddToWishListRequest(_message.Message):
    __slots__ = ("item_id", "buyer_address")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    BUYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    buyer_address: str
    def __init__(self, item_id: _Optional[int] = ..., buyer_address: _Optional[str] = ...) -> None: ...

class AddToWishListResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class RateItemRequest(_message.Message):
    __slots__ = ("item_id", "buyer_address", "rating")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    BUYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    buyer_address: str
    rating: int
    def __init__(self, item_id: _Optional[int] = ..., buyer_address: _Optional[str] = ..., rating: _Optional[int] = ...) -> None: ...

class RateItemResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class ItemNotificationRequest(_message.Message):
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

class ItemNotificationResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...
