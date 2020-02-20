#!/usr/bin/env python3

from flask import Flask
from flask_jwt_extended import JWTManager
from app_config import app_config
from flask_restful import Api
from resources.login import Login

app = Flask(__name__)
app.config["SECRET_KEY"] = app_config["secret_key"]
api = Api(app)
jwt = JWTManager(app)

api.add_resource(Login, '/login')

if __name__=="__main__":
  print(app.config["SECRET_KEY"])
  app.run(port=5000, debug=True)
  