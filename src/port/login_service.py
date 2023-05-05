from typing import Union
from src.port.auth_service import IAuthService
from src.port.user_repository import IUserRepository
from src.typing import session_token


class ILoginService():
    def __init__(self, user_repository: IUserRepository, auth_service: IAuthService) -> None:
        pass

    def login(self, login_dto: dict) -> Union[session_token, None]:
        pass
