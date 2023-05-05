from abc import ABC, abstractmethod
from src.typing import session_token


class IAuthRepository(ABC):
    @abstractmethod
    def get(self, user_id: str) -> session_token:
        pass

    @abstractmethod
    def add(self, user_id: str, session_token: session_token, expiration_time: int):
        pass

    @abstractmethod
    def delete(self, user_id: str):
        pass
