from fastapi import FastAPI

from . import schemas, models
from .database import engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post('/blog/create', response_model=schemas.Blog)
def create_blog(request: schemas.Blog):
    return {
        'title': request.title,
        'body': request.body,
    }
