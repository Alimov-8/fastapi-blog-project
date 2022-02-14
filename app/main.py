import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from blog.routers import blogs, users, auths
from blog.database import Base, engine
from blog.graphql import Query, Mutations

app = FastAPI(title="Blog API")

Base.metadata.create_all(bind=engine)

app.include_router(auths.router)
app.include_router(blogs.router)
app.include_router(users.router)


app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutations)))
