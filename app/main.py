import graphene
from fastapi import FastAPI, Body
from starlette.graphql import GraphQLApp
from fastapi.responses import JSONResponse

from blog.routers import blogs, users, auths
from blog.database import Base, engine
from blog.graphql import Query, Mutations
from blog.celery_worker import create_task


app = FastAPI(title="Blog API")


@app.post("/celery", tags=['celery'])
def run_task(data=Body(...)):
    amount = int(data["amount"])
    task = create_task.delay(amount)
    return JSONResponse({"Response": task.get()})


Base.metadata.create_all(bind=engine)

app.include_router(auths.router)
app.include_router(blogs.router)
app.include_router(users.router)


app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutations)))
