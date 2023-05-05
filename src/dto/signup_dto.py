from flask_reqparse import RequestParser

def signup_dto() -> dict:
    parser = RequestParser()
    parser.add_argument('username',type=str,required=True,help='username not passed')
    parser.add_argument('password',type=str,required=True,help='password not passed')
    parser.add_argument('email',type=str,required=True,help='email not passed')
    args = parser.parse_args()
    return args
