from flask_reqparse import RequestParser

def login_dto() -> dict:
    parser = RequestParser()
    parser.add_argument('username',type=str,required=True,help='username not sended')
    parser.add_argument('password',type=str,required=True,help='password not sended')
    args = parser.parse_args()
    return args