from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas
from blog.database import get_db
from blog.views import blogs

router = APIRouter(
    prefix="/blogs",
    tags=["blogs"],
)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blogs.create(request, db)


@router.get('/', response_model=List[schemas.BlogInfo])
def read_blogs(db: Session = Depends(get_db)):
    return blogs.get_all(db)


@router.get('/{id}', response_model=schemas.ShortBlogInfo)
def read_blog(id: int, db: Session = Depends(get_db)):
    return blogs.get_blog_or_404(db, id).first()


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = blogs.get_blog_or_404(db, id)
    return blogs.update(request, db, blog)


@router.delete('/{id}')
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = blogs.get_blog_or_404(db, id)
    return blogs.delete(db, blog)



