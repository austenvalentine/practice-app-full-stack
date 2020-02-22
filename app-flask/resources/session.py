from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timezone
from models.session_model import SessionModel
from models.user_model import UserModel


class Session(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument("session_id", required=True, type=int, help="invalid session id")
  @jwt_required
  def get(self):
    args = parser.parse_args()
    username = get_jwt_identity()

    user = UserModel.get_user_by_username(username)

    session = SessionModel.get_session_by_id(args["session_id"], user.id)
    if session:
      return session.json()
    return {"message": "invalid session id"}, 400

  @jwt_required
  def post(self):
    username = get_jwt_identity()
    user = UserModel.get_user_by_username(username)
    

    parser = reqparse.RequestParser()
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
    args = parser.parse_args()
    print(">>>>>>>>>>>>>>>>>>>>", args)
    SessionModel.create_session(
      user_id=user.id,
      focus=args["focus"],
      win=args["win"],
      challenge=args["challenge"],
      next_step=args["next_step"]
    )
