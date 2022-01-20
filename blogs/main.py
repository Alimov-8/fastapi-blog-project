from fastapi import FastAPI, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import schemas, models, hashing
from .database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog/create', status_code=status.HTTP_201_CREATED)
def create_new_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blogs', response_model=List[schemas.BlogInfo])
def read_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShortBlog)
def read_blog(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        return blog

    response.status_code = status.HTTP_404_NOT_FOUND
    return {
        "detail": f"Blog with the id {id} is not available"
    }


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if blog.first():
        blog.update(request.dict(), synchronize_session=False)
        db.commit()
        return {
            "detail": "Successfully updated"
        }

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Blog with the id {id} is not available")


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if blog.first():
        blog.delete(synchronize_session=False)
        db.commit()
        return {
            "detail": "Successfully deleted"
        }

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Blog with the id {id} is not available")


@app.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=hashing.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
