from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.session_model import SessionModel

class Sessions(Resource):
  @jwt_required
  def get(self):
    user_id = get_jwt_identity()
    sessions = SessionModel.get_sessions_by_user_id(user_id)
    return [session.json() for session in sessions], 200
