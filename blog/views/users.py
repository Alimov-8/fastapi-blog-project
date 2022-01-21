from fastapi import status, HTTPException

from blog import models, hashing


def create(db, request):
    new_user = models.User(name=request.name, email=request.email, password=hashing.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_or_404(db, id):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")

    return user

