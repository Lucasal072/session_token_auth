from src.port.hash_service import IHashService
from bcrypt import checkpw, hashpw


class BcryptHashService(IHashService):

    def __init__(self, salt: bytes) -> None:
        self.salt = salt

    def hashed_password(self, password: str) -> bytes:
        hashed_password = hashpw(password.encode(), self.salt)
        return hashed_password

    def check_password(self, password: str, hashed_password: str) -> bool:
        check_password = checkpw(password.encode(),hashed_password)
        return check_password
