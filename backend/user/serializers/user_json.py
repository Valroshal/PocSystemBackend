from dataclasses import dataclass

from backend.core.base_serializer import BaseJsonSerializer


@dataclass
class UserJson(BaseJsonSerializer):
    id: str
    email: str

