from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from models.user import UserModel


parser = reqparse.RequestParser()
parser.add_argument("username", type=str, help="invalid username")
parser.add_argument("password", type=str, help="invalid password")

class Login(Resource):
  def post(self):
    args = parser.parse_args()
    user = UserModel.get_user_by_name(args["username"])
    if user.verify_password(args["password"]):
      user_token = create_access_token(identity=user.username)
      return {"access_token":user_token}, 200
    return {"message": "invalid username or password"},401