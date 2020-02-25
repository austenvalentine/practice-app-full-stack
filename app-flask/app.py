#!/usr/bin/env python3

from flask import Flask
from flask_jwt_extended import JWTManager
from app_config import app_config
from flask_restful import Api
from resources.login import Login
from resources.focus_session import Focus
from resources.focus_sessions import FocusSessions

app = Flask(__name__)
app.config["SECRET_KEY"] = app_config["secret_key"]
# enable token expiration after initial testing
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
api = Api(app)
jwt = JWTManager(app)

api.add_resource(Login, '/login')
api.add_resource(Focus, '/focus_session/<int:focus_session_id>', '/focus_session')
api.add_resource(FocusSessions, '/focus_sessions')

if __name__=="__main__":
  print(app.config["SECRET_KEY"])
  app.run(port=5000, debug=True)
  