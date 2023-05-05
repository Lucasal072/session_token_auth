from src.port.auth_service import IAuthService
from src.port.auth_repository import IAuthRepository
from src.utils import decodebase64url,encodebase64url
from src.typing import session_token,user_id
from typing import Union
from datetime import datetime,timedelta
from json import dumps,loads

class SessionAuthService(IAuthService):

    def __init__(self,expiration_time:int,auth_repository:IAuthRepository) -> None:
        self.expiration_time = expiration_time
        self.auth_repository = auth_repository

    def get_identify(self,session_token:session_token) -> user_id:
        decoded_session_token = decodebase64url(session_token)
        if not decoded_session_token:
            return
        session_token_json = loads(decoded_session_token)
        return session_token_json.get('user_id')

    def create_token(self,user_id:str) -> session_token:
        session_token = self.__generate_token(user_id)
        self.__save_token(user_id,session_token)
        return session_token

    def check_token(self,user_id:str,session_token:session_token) -> bool:
        token = self.__get_token(user_id)
        if not token:
            return False
        return token == session_token
        
    def revoke_token(self,user_id:str) -> None:
        self.auth_repository.delete(user_id)

    def __get_token(self,user_id:str) -> Union[session_token,None]:
        token = self.auth_repository.get(user_id)
        if not token:
            return None
        return token.decode()


    def __save_token(self,user_id:str,session_token:session_token) -> None:
        self.auth_repository.add(user_id,session_token,self.expiration_time)

    def __generate_token(self,user_id:str) -> session_token:
        token = self.__get_token(user_id)
        if token:
            return token
        expiration_time = datetime.utcnow() + timedelta(seconds=self.expiration_time)
        session_token = {'user_id':user_id,
        'expiration_time':int(expiration_time.timestamp())}
        return encodebase64url(dumps(session_token))