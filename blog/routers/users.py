from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from blog import schemas, database
from blog.views import users

router = APIRouter(
    prefix="/users",
    tags=["user"],
)


@router.post('/create', response_model=schemas.UserInfo)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return users.create(db, request)


@router.get('/{id}', response_model=schemas.UserInfo)
def read_user(id: int, db: Session = Depends(database.get_db)):
    return users.get_user_or_404(db, id).first()
