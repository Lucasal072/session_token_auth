from src.port.user_repository import IUserRepository
from src.port.auth_service import IAuthService
from src.port.hash_service import IHashService
from src.typing import session_token
from typing import Union
from functools import cache


class LoginService():
    def __init__(self, user_repository: IUserRepository, auth_service: IAuthService, hash_service: IHashService) -> None:
        self.user_repository = user_repository
        self.auth_service = auth_service
        self.hash_service = hash_service

    def login(self, login_dto: dict) -> Union[session_token, None]:
        if not self.__check_credentials(login_dto):
            return
        session_token = self.__generate_sesion_token(login_dto)
        return session_token

    def __check_credentials(self, login_dto: dict) -> bool:
        username = login_dto.get('username')
        user = self.__get_user(username)
        if not user:
            return False
        password = login_dto.get('password')
        hashed_password = user.get('password')
        if not self.__check_password(hashed_password, password):
            return False
        return True

    @cache
    def __get_user(self, username: str) -> Union[dict, None]:
        user_data = self.user_repository.get(username)
        return user_data

    def __check_password(self, hashed_password: str, password: str) -> bool:
        return self.hash_service.check_password(password, hashed_password)

    def __generate_sesion_token(self, login_dto: dict) -> Union[session_token, None]:
        username = login_dto.get('username')
        user = self.__get_user(username)
        if not user:
            return
        user_id = user.get('_id')
        return self.auth_service.create_token(str(user_id))
