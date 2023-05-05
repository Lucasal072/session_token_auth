from src.port.user_repository import IUserRepository
from src.entity.user import User
from flask_pymongo import PyMongo


class MongoUserRepository(IUserRepository):

    def __init__(self, mongo: PyMongo) -> None:
        self.mongo = mongo

    def get(self, username: str):
        return self.mongo.db.user.find_one({'username': username})

    def add(self, entity: User) -> None:
        user_document = {'username': entity.username,
                         'password': entity.password,
                         'email': entity.email}
        self.mongo.db.user.insert_one(user_document)

    def update(self, user_id: str, entity):  # refactor this
        self.mongo.db.user.update_one(
            filter={'user_id': user_id}, update=entity)

    def delete(self, user_id: str):
        self.mongo.db.user.delete_one({'user_id': user_id})
