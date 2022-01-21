from fastapi import Response, status, HTTPException

from blog import models


def get_all(db):
    blogs = db.query(models.Blog).all()
    return blogs


def get_blog_or_404(db, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog


def create(request, db):
    new_blog = models.Blog(title=request.title, body=request.body, creator_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update(request, db, blog):
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return {
        "detail": "Successfully updated"
    }


def delete(db, blog):
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

