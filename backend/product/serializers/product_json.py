from dataclasses import dataclass

from unicodedata import decimal
from backend.core.base_serializer import BaseJsonSerializer


@dataclass
class ProductJson(BaseJsonSerializer):
    id: str
    name: str
    description: str
    price: decimal
    quantity: int
    favorite: bool
