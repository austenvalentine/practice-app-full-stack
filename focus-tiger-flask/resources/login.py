from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from models.user_model import UserModel


parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True,help="invalid username")
parser.add_argument("password", type=str, required=True, help="invalid password")

class Login(Resource):
  def post(self):
    args = parser.parse_args()
    user = UserModel(username=args["username"]).get_by_username()
    print("user:", user.json())
    if user and user.verify_password(args["password"]):
      user_token = create_access_token(identity=user.id)
      return {"access_token":user_token}, 200
    return {"message": "invalid username or password"}, 401