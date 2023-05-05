from abc import ABC, abstractmethod


class IHashService(ABC):
    @abstractmethod
    def hashed_password(self, password: str) -> bytes:
        pass

    @abstractmethod
    def check_password(self, password: str, hashed_password: str) -> bool:
        pass
