from src import app, session_auth_service
from src.decorators.protected_route import protected_route
from flask import request, Response



@app.route('/auth/logout', methods=['DELETE'])
@protected_route(session_auth_service)
def logout():
    headers = request.headers
    session_token = headers.get('Authorization')
    user_id = session_auth_service.get_identify(session_token)
    session_auth_service.revoke_token(user_id)
    return Response("Token has revoked",200)
