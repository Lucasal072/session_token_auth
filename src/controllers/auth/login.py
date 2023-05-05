from src import app,user_repository,session_auth_service,bcypt_hash_service
from src.service.auth.login_service import LoginService
from src.dto.login_dto import login_dto
from flask import request, Response


@app.route('/auth/login', methods=['POST'])
def login():
    login_data = login_dto()
    login_service = LoginService(user_repository,session_auth_service,bcypt_hash_service)
    session_token = login_service.login(login_data)
    if not session_token:
        Response('Unauthorized User',401)     
    return Response(session_token,200)