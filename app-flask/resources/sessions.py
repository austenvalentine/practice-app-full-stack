from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.session_model import SessionModel
from models.user_model import UserModel

class Sessions(Resource):
  @jwt_required
  def get(self):
    username = get_jwt_identity()
    user = UserModel.get_user_by_username(username)
    sessions = SessionModel.get_sessions_by_user_id(user.id)
    return [session.json() for session in sessions], 200
