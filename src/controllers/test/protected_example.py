from src import app,session_auth_service
from src.decorators.protected_route import protected_route
from flask import request, Response


@app.route('/protected', methods=['GET'])
@protected_route(session_auth_service)
def protected_example():
    return Response("Hello World",200)
