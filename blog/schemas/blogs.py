from pydantic import BaseModel

from blog.schemas.users import ShortUserInfoSchema


class BlogBaseSchema(BaseModel):
    title: str
    body: str


class BlogSchema(BlogBaseSchema):
    class Config:
        orm_mode = True


class ShortBlogInfoSchema(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class BlogInfoSchema(BaseModel):
    id: int
    title: str
    body: str
    creator: ShortUserInfoSchema

    class Config:
        orm_mode = True
