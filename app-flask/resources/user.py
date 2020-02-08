from flask_restful import Resource, reqparse, abort
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    fresh_jwt_required
)
from models.user_model import UserModel
from .passlib_setup import encrypt_password, verify_password

# setup parsers
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

_user_login_parser = reqparse.RequestParser()
_user_login_parser.add_argument(
    "username",
    type=str,
    help="username/email required"
)
_user_login_parser.add_argument(
    "password",
    type=str,
    help="password required"
)

# api resources
class UserRegister(Resource):
    def post(self):
        args = _user_register_parser.parse_args()
        username = args["username"]
        email = args["email"]
        hashed_password = encrypt_password(args["password"])
        if UserModel.find_by_username(username) or UserModel.find_by_email(email):
            abort(400, message={"error": "username or email exists"})
        elif not args["email"] or not args["username"] or not args["password"]:
            abort(400, message={"error": "Fields cannot be left blank."})
        
        new_user = UserModel(username, email, hashed_password)
        new_user.add()
        return "User added!", 200

    @fresh_jwt_required
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
        return [user.json() for user in UserModel.query.all()]


class UserLogin(Resource):
    def post(self):
        args = _user_login_parser.parse_args()
        username = args["username"]
        password =  args["password"]
        user = UserModel.find_by_username(username) if UserModel.find_by_username(username) else UserModel.find_by_email(username)

        print("LOGIN:", password)
        print("USER", user.hash_pw)
        if not user or not verify_password(password, user.hash_pw):
            abort(400, message={"error":"invalid username, email or password"})

        token = create_access_token(identity=user.idkey, fresh=True)
        return {
            "access_token": token
        }, 200
        
        
