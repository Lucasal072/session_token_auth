from src import app,user_repository,bcypt_hash_service
from src.dto.signup_dto import signup_dto
from src.service.auth.signup_service import SignupService
from flask import request, Response


@app.route('/auth/signup', methods=['POST'])
def signup():
    signup_data = signup_dto()
    signup_service = SignupService(user_repository,bcypt_hash_service)
    if not signup_service.signup(signup_data):
        return Response('User is not registered',401)
    return Response('User is registered',200)