import graphene

from .database import get_db
from .schemas.users import UserModel
from .repository import users, blogs

db = get_db()


class BlogRequest:
    def __init__(self, title, body, creator_id):
        self.title = title
        self.body = body
        self.id = creator_id


class UserRequest:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Query(graphene.ObjectType):

    all_users = graphene.List(UserModel)
    user_by_id = graphene.Field(UserModel, id=graphene.Int(required=True))

    def resolve_all_users(self, info):
        query = UserModel.get_query(info)
        return query.all()

    def resolve_user_by_id(self, info, id):
        return users.get_user_or_404(db, id).first()


class UserMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    response = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, name, email, password):
        users.create(db, request=UserRequest(name, email, password))
        response = 'User Created Successfully!'
        return UserMutation(response=response)


class BlogMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        creator_id = graphene.Int(required=True)

    response = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, title, body, creator_id):
        request = BlogRequest(title, body, creator_id)
        blogs.create(request, db, request)
        response = 'Blog Created Successfully!'
        return UserMutation(response=response)


class Mutations(graphene.ObjectType):
    create_new_user = UserMutation.Field()
    create_new_blog = BlogMutation.Field()


