from models.user_model import UserModel
from flask_restful import Resource, reqparse
from validate_email import validate_email

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="username is required" )
parser.add_argument("email", type=str, required=True, help="email is required")
parser.add_argument("password", type=str, required=True, help="password is required")

class Register(Resource):
  def post(self):
    args = parser.parse_args()
    password = args["password"].lower()
    if UserModel.user_exists(args["username"], args["email"]):
      return {"message":"user exists"}, 400

    if validate_email(email, verify=True):
      console.log(">>>>>>>>>>>>>!!!!VALID EMAIL!")
    else:
      return {"message": "invalid email address"}, 400

    if len(args["password"]) < 10:
      return {"message":"password must be at least 10 characters"}, 400

    acc = {}
    for ch in args["password"]:
      if acc.get[ch, None]:
        acc[ch]++
      else: 
        acc[ch] = 0
      
    if len(acc.key() < 6):
      return {"message" : "password must contain at least 6 different symbols"}, 400


    


