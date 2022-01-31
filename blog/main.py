from fastapi import FastAPI

from .routers import blogs, users, auths
from .database import engine, Base


app = FastAPI(title="Blog API")

Base.metadata.create_all(bind=engine)

app.include_router(auths.router)
app.include_router(blogs.router)
app.include_router(users.router)
