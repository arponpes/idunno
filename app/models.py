from typing import TypeVar, Optional
from pydantic import BaseModel


T = TypeVar("T")


class Card(BaseModel):
    id: str = None
    spanish: str
    chinese: str
    pinyin: str


class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None
