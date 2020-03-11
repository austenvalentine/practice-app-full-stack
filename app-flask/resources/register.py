from models.user_model import UserModel
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="username is required" )
parser.add_argument("email", type=str, required=True, help="email is required")
parser.add_argument("password", type=str, required=True, help="password is required")

class Register(Resource):
  def post(self):
    args = parser.parse_args()
    if UserModel.getUserByUsername():
      return {"message": "error: username is taken"}
    else:
      return 400

