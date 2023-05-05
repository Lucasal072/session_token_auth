from dataclasses import dataclass


@dataclass
class User:
    email: str
    username: str
    password: str