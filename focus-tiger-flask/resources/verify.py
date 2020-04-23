from flask_restful import Resource, reqparse
from models.registrant_model import RegistrantModel
from models.user_model import UserModel

parser = reqparse.RequestParser()
parser.add_argument("token", type=str, required=True, help="missing token")

class Verify(Resource):
  def get(self):
    args = parser.parse_args()
    token = args["token"]
    registrant = RegistrantModel(token=token).get_by_token()
    if registrant:
      user = UserModel(
        username=registrant.username,
        email=registrant.email,
        passhash=registrant.passhash
      ).add()
      registrant.delete()
      return {
        "message": "email verified",
      }

