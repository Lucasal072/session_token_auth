from typing import Callable
from src.port.auth_service import IAuthService
from functools import wraps
from flask import request, Response


def protected_route(auth_service: IAuthService):
    def decorator(func:Callable,/):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Response:
            headers = request.headers
            session_token = headers.get('Authorization')
            if not session_token:
                return Response('Not has session token in Authorization headers ', 401)
            user_id = auth_service.get_identify(session_token)
            if not user_id or  not auth_service.check_token(user_id,session_token):
                return Response('session token is not valid', 401)
            response = func(*args, **kwargs)
            return response
        return wrapper
    return decorator
