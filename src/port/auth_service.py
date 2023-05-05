from abc import ABC, abstractmethod
from typing import Union
from src.typing import session_token,user_id


class IAuthService(ABC):
    @abstractmethod
    def get_identify(self,session_token:session_token) -> user_id:
        pass

    @abstractmethod
    def create_token(self, user_id: str) -> session_token:
        pass

    @abstractmethod
    def check_token(self, user_id: str, session_token: session_token) -> bool:
        pass

    @abstractmethod
    def revoke_token(self, user_id: str) -> None:
        pass
