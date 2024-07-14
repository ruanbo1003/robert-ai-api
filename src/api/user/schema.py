
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserLogin(BaseModel):
    name: str
    password: str


class UserSignup(BaseModel):
    name: str
    password: str


class UserExist(BaseModel):
    name: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
