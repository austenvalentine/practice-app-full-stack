from flask_restful import Resource
from models.user import UserModel
class Login(Resource):
  def get(self):
    firstUser = UserModel.get_user_by_id(2)
    return firstUser.json(), 200