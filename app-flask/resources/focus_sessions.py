from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.focus_model import FocusModel

class Focuss(Resource):
  @jwt_required
  def get(self):
    user_id = get_jwt_identity()
    focus_sessions = FocusModel.get_focus_sessions_by_user_id(user_id)
    return [focus_session.json() for focus_session in focus_sessions], 200