from fastapi import Response, status, HTTPException

from ..models.blogs import Blog


def get_all(db):
    blogs = db.query(Blog).all()
    return blogs


def get_blog_or_404(db, id: int):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog


def create(request, db, user):
    new_blog = Blog(title=request.title, body=request.body, creator_id=user.id)
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


def is_creator(blog, user):
    if blog.first().creator_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"You don't have permission to edit blog with the id {id}")
    return True

