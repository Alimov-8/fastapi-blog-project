from fastapi import FastAPI

from blog.routers import blogs, users, auths
from blog.database import engine, Base


app = FastAPI(title="Blog API")

Base.metadata.create_all(bind=engine)

app.include_router(auths.router)
app.include_router(blogs.router)
app.include_router(users.router)
