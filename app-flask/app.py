#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"


if __name__=='__main__':
    from db import db   
    db = SQLAlchemy(app)
