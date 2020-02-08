#!/usr/bin/env python3
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.session import Session, Sessions
from resources.user import UserLogin, UserRegister, UserList
from db import db
import app_config

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = app_config.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = app_config.database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)
jwt = JWTManager(app)
db.init_app(app)

@app.before_first_request
def setup_app():
    db.create_all()

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserList, '/userlist')
api.add_resource(Session, '/session/<userid>/<sessionid>')
api.add_resource(Sessions, '/sessions/<userid>')

if __name__=="__main__":
    app.run(port=5000, debug=True)