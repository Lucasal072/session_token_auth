from abc import ABC, abstractmethod


class IUserRepository(ABC):

    @abstractmethod
    def get(self, username: str):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def update(self, user_id: str, entity):
        pass

    @abstractmethod
    def delete(self, user_id: str):
        pass
