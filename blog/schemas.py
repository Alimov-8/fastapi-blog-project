from pydantic import BaseModel
from typing import List, Optional


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShortUserInfo(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class UserInfo(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class ShortBlogInfo(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class BlogInfo(BaseModel):
    id: int
    title: str
    body: str
    creator: ShortUserInfo

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
