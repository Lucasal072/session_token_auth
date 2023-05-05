from src.port.hash_service import IHashService
from src.port.user_repository import IUserRepository



class ISignupService():
    def __init__(self, user_repository: IUserRepository, hash_service: IHashService) -> None:
        pass

    def signup(self, signup_dto: dict) -> bool:
        pass
