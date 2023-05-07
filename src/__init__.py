from flask import Flask
from flask_pymongo import PyMongo
from bcrypt import gensalt
from src.repositories.auth_repository import RedisAuthRepository
from src.repositories.user_repository import MongoUserRepository
from src.service.auth.session_auth_service import SessionAuthService
from src.service.hash.bcrypt_hash_service import BcryptHashService
from src.config.settings import EXPIRATION_SESSION_TOKEN_IN_SECONDS


app = Flask(__name__)
app.config.from_object('src.config.settings')
mongo = PyMongo(app)
user_repository = MongoUserRepository(mongo)
bcypt_hash_service = BcryptHashService(gensalt())
redis_repository = RedisAuthRepository()
session_auth_service = SessionAuthService(
    EXPIRATION_SESSION_TOKEN_IN_SECONDS, redis_repository)

from src.controllers.auth import *
from src.controllers.test import *
