from src import app
from flask import request, Response


@app.route('/protected', methods=['GET'])
def protected_example():

    return Response()
