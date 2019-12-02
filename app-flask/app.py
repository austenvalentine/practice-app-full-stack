#!/usr/bin/env python3
from flask import Flask
from resources.session import Session
from resources.user import User
from db import db
import app_config

app = Flask(__name__)
app.config['SECRET_KEY'] = app_config.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = app_config.database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def setup_app():
    db.create_all()

if __name__=="__main__":
    app.run(port=5000, debug=True)