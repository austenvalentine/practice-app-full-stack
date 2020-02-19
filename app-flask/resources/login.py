from flask_restful import Resource
from models.user import UserModel
class Login(Resource):
  def get(self):
    return {"message": "Hello World!"}, 200