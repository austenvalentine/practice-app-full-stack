from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.session_model import SessionModel
from models.user_model import UserModel

parser = reqparse.RequestParser()
parser.add_argument("session_id", required=True, type=int, help="invalid session id")

class Session(Resource):
  @jwt_required
  def get(self):
    args = parser.parse_args()
    username = get_jwt_identity()

    user = UserModel.get_by_username(username)

    session = SessionModel.get_session_by_id(args["session_id"], user.id)
    if session:
      return session.json()
    return {"message": "invalid session id"}, 400
