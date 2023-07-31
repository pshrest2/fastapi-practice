from pydantic import BaseModel
from .item import Item


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    items: list[Item] = []

    class Config:
        from_attributes = True
