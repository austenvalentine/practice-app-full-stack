from flask_restful import Resource
from models.registrant_model import RegistrantModel
from models.user_model import UserModel

class Verify(Resource):
  def get(self, token):
    registrant = RegistrantModel(token=token)
    registrant.get_by_token()
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

