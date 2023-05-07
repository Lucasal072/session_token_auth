from src.port.auth_repository import IAuthRepository
from src.typing import session_token
from redis import Redis


class RedisAuthRepository(IAuthRepository):

    def __init__(self, host: str, port: int, database: str, password: str) -> None:
        self.redis = Redis(host, port, database, password)

    def get(self, user_id: str) -> session_token:
        return self.redis.get(user_id)

    def add(self, user_id: str, session_token: bytes, expiration_time: int) -> None:
        self.redis.set(user_id, session_token, ex=expiration_time)

    def delete(self, user_id: str) -> None:
        self.redis.delete(user_id)
