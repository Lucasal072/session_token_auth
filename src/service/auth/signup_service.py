from src.port.hash_service import IHashService
from src.port.user_repository import IUserRepository
from src.entity.user import User
import re

REGEX_EMAIL = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

class SignupService():
    def __init__(self, user_repository: IUserRepository, hash_service: IHashService) -> None:
        self.user_repository = user_repository
        self.hash_service = hash_service

    def signup(self, signup_dto: dict) -> bool:
        user = User(**signup_dto)
        if not self.__credentials_valid(user):
            return False
        user.password = self.__hash_password(user.password)
        self.user_repository.add(user)
        return True
        
    def __hash_password(self,password:str) -> bytes:
        return self.hash_service.hashed_password(password)

    def __credentials_valid(self, user: User) -> bool:
        if not self.__password_valid(user.password):
            return False
        if not self.__email_valid(user.email):
            return False
        if not self.__username_valid(user.username):
            return False
        return True

    def __password_valid(self, password: str) -> bool:
        if len(password) < 8:
            return False
        return True

    def __username_valid(self, username)-> bool:
        if len(username) < 3:
            return False
        if self.user_repository.get(username):
            return False
        return True
                    
    def __email_valid(self, email)-> bool:
        if len(email) < 7:
            return False
        if not re.fullmatch(REGEX_EMAIL,email):
            return False
        return True
