from fastapi import FastAPI, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session

from . import schemas, models
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


@app.get('/blogs')
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog_info(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        return blog

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Blog with the id {id} is not available")

    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {
    #     "detail": f"Blog with the id {id} is not available"
    # }
