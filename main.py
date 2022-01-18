from fastapi import FastAPI
from typing import Optional


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


@app.get('/blogs/{blog_id}')
def show_blog_info(blog_id: int):
    # fetch blog with id = id
    return {
        'data': blog_id
    }


@app.get('/blogs/{blog_id}/comments')
def show_comments_of_blog(blog_id):
    return {
        'data': {
            'blog_id': blog_id,
            'comments': ['1', '2'],
        }
    }
