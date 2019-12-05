from flask_restful import Resource, reqparse, abort
from models.user_model import UserModel
from .security import encrypt_password, verify_password

_user_register_parser = reqparse.RequestParser()
_user_register_parser.add_argument(
    "username",
    type=str,
    help="username or email is required"
)
_user_register_parser.add_argument(
    "email",
    type=str,
    help="username or email is required"
)
_user_register_parser.add_argument(
    "password",
    type=str,
    help="password is required"
)


class UserRegister(Resource):
    def post(self):
        args = _user_register_parser.parse_args()
        username = args["username"]
        email = args["email"]
        password = args["password"]
        if UserModel.find_by_username(username) or UserModel.find_by_email(email):
            abort(400, message={"error": "username or email exists"})
        elif not args["email"] or not args["username"] or not args["password"]:
            abort(400, message={"error": "Fields cannot be left blank."})
        
        new_user = UserModel(username, email, password)
        new_user.add()
        return "User added!", 200

    def delete(self):
        args = _user_register_parser.parse_args()
        username = args["username"]
        user_to_delete = UserModel.find_by_username(username)
        if not user_to_delete:
            abort(400, message={"error":"There is no such user to delete."})
        user_to_delete.delete()
        return "User deleted!", 200

class UserList(Resource):
    def get(self):
        return [user.json() for user in UserModel.query.filter_by().all()]


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        ""
    )