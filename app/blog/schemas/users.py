from graphene_sqlalchemy import SQLAlchemyObjectType
from pydantic import BaseModel
from typing import List
from ..models.users import User


class UserSchema(BaseModel):
    name: str
    email: str
    password: str


class ShortUserInfoSchema(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class ShortBlogInfoSchema(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class UserInfoSchema(BaseModel):
    name: str
    email: str
    blogs: List[ShortBlogInfoSchema] = []

    class Config:
        orm_mode = True


class UserModel(SQLAlchemyObjectType):
    class Meta:
        model = User
