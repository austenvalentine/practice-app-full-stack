#!/usr/bin/env python3

from flask import Flask
from flask_jwt_extended import JWTManager
from app_config import app_config
from flask_restful import Api
from resources.login import Login
from resources.session import Session
from resources.sessions import Sessions

app = Flask(__name__)
app.config["SECRET_KEY"] = app_config["secret_key"]
# enable token expiration after initial testing
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
api = Api(app)
jwt = JWTManager(app)

api.add_resource(Login, '/login')
api.add_resource(Session, '/session')
api.add_resource(Sessions, '/sessions')

if __name__=="__main__":
  print(app.config["SECRET_KEY"])
  app.run(port=5000, debug=True)
  