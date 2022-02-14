import graphene

from .models.users import User
from . import hashing, database
from .schemas.users import UserModel
from .repository.users import get_user_or_404

db = database.get_db()


class Query(graphene.ObjectType):

    all_users = graphene.List(UserModel)
    user_by_id = graphene.Field(UserModel, id=graphene.Int(required=True))

    def resolve_all_users(self, info):
        query = UserModel.get_query(info)
        return query.all()

    def resolve_user_by_id(self, info, id):
        return get_user_or_404(db, id).first()


class UserMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    response = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, name, email, password):
        new_user = User(name=name,
                        email=email,
                        password=hashing.get_password_hash(password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        response = 'User Created Successfully!'
        return UserMutation(response=response)


class Mutations(graphene.ObjectType):
    create_new_user = UserMutation.Field()


