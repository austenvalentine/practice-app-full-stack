from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timezone
from models.session_model import SessionModel

# This function reuses the add_argument declaratons because the args for get and put are very similar.
def parse_get_put_args(parser):
  parser.add_argument(
    "focus", required=True, type=str, help="invalid focus",
  )
  parser.add_argument(
    "win", required=True, type=str, help="invalid win",
  )
  parser.add_argument(
    "challenge", required=True, type=str, help="invalid challenge",
  )
  parser.add_argument(
    "next_step", required=True, type=str, help="invalid next_step",
  )
  return parser.parse_args()

class Session(Resource):
  @jwt_required
  def get(self):
    user_id = get_jwt_identity()
    parser = reqparse.RequestParser()
    parser.add_argument("session_id", required=True, type=int, help="invalid session id")
    args = parser.parse_args()

    session = SessionModel.get_session_by_id(args["session_id"], user_id)
    if session:
      return session.json()
    return {"message": "invalid session id"}, 400

  @jwt_required
  def post(self):
    user_id = get_jwt_identity()

    parser = reqparse.RequestParser()
    args = parse_get_put_args()
    SessionModel.create_session(
      user_id=user_id,
      focus=args["focus"],
      win=args["win"],
      challenge=args["challenge"],
      next_step=args["next_step"]
    )

  @jwt_required
  def put(self):
    user_id = get_jwt_identity()
    parser = reqparse.RequestParser()
    parser.add_argument('session_id', required=True, type=int, help="invalid session id")
    args = parse_get_put_args(parser)
    return args
    