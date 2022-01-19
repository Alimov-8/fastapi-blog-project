from fastapi import FastAPI

from blogs import schemas


app = FastAPI()


@app.post('/blog/create', response_model=schemas.Blog)
def create_blog(request: schemas.Blog):
    return {
        'title': request.title,
        'body': request.body,
    }
