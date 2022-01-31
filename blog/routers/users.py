from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import database
from ..repository import users
from ..schemas.users import UserSchema, UserInfoSchema

router = APIRouter(
    prefix="/users",
    tags=["user"],
)


@router.post('/create', response_model=UserInfoSchema)
def create_user(request: UserSchema, db: Session = Depends(database.get_db)):
    return users.create(db, request)


@router.get('/{id}', response_model=UserInfoSchema)
def read_user(id: int, db: Session = Depends(database.get_db)):
    return users.get_user_or_404(db, id).first()
