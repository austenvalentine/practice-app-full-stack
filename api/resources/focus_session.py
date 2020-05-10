from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timezone
from models.focus_model import FocusModel

parser = reqparse.RequestParser()
parser.add_argument(
  "focus",
  required=True,
  type=str,
  help="invalid focus",
)
parser.add_argument(
  "win",
  required=True,
  type=str,
  help="invalid win",
)
parser.add_argument(
  "challenge",
  required=True,
  type=str,
  help="invalid challenge",
)
parser.add_argument(
  "next_step",
  required=True,
  type=str,
  help="invalid next step",
)

class Focus(Resource):
  @jwt_required
  def get(self, focus_session_id):
    user_id = get_jwt_identity()
    focus_session = FocusModel(_id=focus_session_id, user_id=user_id)
    focus_session.get_by_id()
    if focus_session:
      return focus_session.json()
    return {"message": "invalid focus_session id"}, 400

  @jwt_required
  def post(self):
    user_id = get_jwt_identity()
    args = parser.parse_args()
    result = FocusModel(
      user_id=user_id,
      focus=args["focus"],
      win=args["win"],
      challenge=args["challenge"],
      next_step=args["next_step"]
    ).add()

    if result:
      return {"message" : "focus session successfully added"}, 200
    else: 
      return {"message" : "data input failed"}, 400

  @jwt_required
  def put(self, focus_session_id):
    user_id = get_jwt_identity()
    args = parser.parse_args()
    focus_session = FocusModel(_id=focus_session_id, user_id=user_id)
    if not focus_session.get_by_id():
      return {"message": "invalid focus session id"}, 400
    focus_session.focus     = args["focus"],
    focus_session.win       = args["win"],
    focus_session.challenge = args["challenge"],
    focus_session.next_step = args["next_step"]
    result = focus_session.update()
    if result:
      return {"message":"focus session successfully updated"}, 200
    else: 
      return {"message" : "input data failed database check"}, 400
    
  @jwt_required
  def delete(self, focus_session_id):
    user_id = get_jwt_identity()
    focus_session = FocusModel(_id=focus_session_id, user_id=user_id)
    if not focus_session.exists():
      return {"message": "invalid focus session id"}, 400
    focus_session.delete()
    return {"message":"focus session successfully deleted"}