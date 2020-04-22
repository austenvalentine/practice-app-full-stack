from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument("token", type=str, required=True, help="missing token")

class Verify(Resource):
  def get(self):

    # lookup token in registrant table
    # copy username, email, encrypted password
    # add new user
    args = parser.parse_args()
    token = args["token"]
    return {
      "message": "email verified",
      "token" : token
    }