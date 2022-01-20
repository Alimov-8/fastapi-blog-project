from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class ShortBlog(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class BlogInfo(BaseModel):
    id: int
    title: str
    body: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str
