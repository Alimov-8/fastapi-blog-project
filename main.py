from typing import Optional

# import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get('/', include_in_schema=False)  # path operation decorator, operation, path
def index():  # path operation function
    return "WELCOME TO BLOG API SYSTEM"


# Query Parameters, required and not required
@app.get('/blogs')
def get_blogs_list(limit: int, published: bool = True, sort: Optional[str] = None):
    if published:
        return {
            'data': f'{limit} published blogs from database'
        }
    return {
        'data': f'{limit} blogs from database'
    }


# Order matters when we have "blogs/unpublished" and "blogs/{blogs_id}"
@app.get('/blogs/unpublished')
def get_unpublished_blogs_list():
    return {
        'data': {
            'detail': 'Unpublished list of blogs',
        }
    }


@app.get('/blogs/{id}')
def show_blog_info(id: int):
    # fetch blog with id = id
    return {
        'data': id
    }


@app.get('/blogs/{blog_id}/comments')
def show_comments_of_blog(id: int):
    return {
        'data': {
            'blog_id': id,
            'comments': ['1', '2'],
        }
    }


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blogs/create', response_model=Blog)
def create_new_blog(blog: Blog):
    return {
        'title': blog.title,
        'body': blog.body,
        'published_at': blog.published_at,
    }


# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8080)
