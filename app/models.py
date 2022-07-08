from typing import TypeVar, Optional
from pydantic import BaseModel


T = TypeVar("T")


class Card(BaseModel):
    id: str = None
    a_side: str
    b_side: str


class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None
