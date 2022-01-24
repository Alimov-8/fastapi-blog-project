from fastapi import status, HTTPException

from blog import models, hashing


def create(db, request):
    new_user = models.User(name=request.name,
                           email=request.email,
                           password=hashing.get_password_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_or_404(db, id: int):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")

    return user


def get_user_by_email(db, email: str):
    for record in db:
        user = record.query(models.User).filter(models.User.email == email)
        if user:
            return user

    return None
