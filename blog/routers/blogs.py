from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import oauth2
from ..repository import blogs
from ..database import get_db
from ..schemas.users import UserSchema
from ..schemas.blogs import BlogSchema, BlogInfoSchema, ShortBlogInfoSchema


router = APIRouter(
    prefix="/blogs",
    tags=["blogs"],
    dependencies=[Depends(oauth2.get_current_user)],
)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_blog(request: BlogSchema,
                db: Session = Depends(get_db),
                user: UserSchema = Depends(oauth2.get_current_user)):
    return blogs.create(request, db, user)


@router.get('/', response_model=List[BlogInfoSchema])
def read_blogs(db: Session = Depends(get_db)):
    return blogs.get_all(db)


@router.get('/{id}', response_model=ShortBlogInfoSchema)
def read_blog(id: int, db: Session = Depends(get_db)):
    return blogs.get_blog_or_404(db, id).first()


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: BlogSchema,
                db: Session = Depends(get_db),
                user: UserSchema = Depends(oauth2.get_current_user)):
    blog = blogs.get_blog_or_404(db, id)
    if blogs.is_creator(blog, user):
        return blogs.update(request, db, blog)


@router.delete('/{id}')
def delete_blog(id: int,
                db: Session = Depends(get_db),
                user: UserSchema = Depends(oauth2.get_current_user)):
    blog = blogs.get_blog_or_404(db, id)
    if blogs.is_creator(blog, user):
        return blogs.delete(db, blog)
