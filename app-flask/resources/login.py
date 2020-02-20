from flask_restful import Resource, reqparse
from models.user import UserModel

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, help="invalid username")

class Login(Resource):
  def get(self):
    args = parser.parse_args()
    user = UserModel.get_user_by_name(args["username"])
    return user.json(), 200