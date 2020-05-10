from models.registrant_model import RegistrantModel
from models.user_model import UserModel
from flask_restful import Resource, reqparse
from helpers.email_helper import send_verify_email

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="username is required" )
parser.add_argument("email", type=str, required=True, help="email is required")
parser.add_argument("password", type=str, required=True, help="password is required")

class Register(Resource):
  def post(self):
    args = parser.parse_args()
    username = args["username"]
    email = args["email"]
    password = args["password"]

    registrant = RegistrantModel(username=username, email=email, password=password)
    ## validation
    if len(username) < 5:
      return {"message": "username must be at least 5 characters"}

    elif UserModel(username=username).exists() or UserModel(email=email).exists():
      return {"message":"user exists"}, 400

    elif len(args["password"]) < 10:
      return {"message":"password must be at least 10 characters"}, 400

    acc = {}
    for ch in args["password"]:
      if acc.get(ch, None):
        acc[ch] = acc[ch] + 1
      else: 
        acc[ch] = 0
      
    if len(acc.keys()) < 6:
      return {"message" : "password must contain at least 6 different symbols"}, 400

    
    # validate email structure before verification
    # if is_valid(email):

    token = send_verify_email(email, username)

    ## add registrant to registrant table
    RegistrantModel(
      username=username,
      email=email,
      password=password,
      token=token
    ).add()

    return {"message": "please verify email"}, 200
    


