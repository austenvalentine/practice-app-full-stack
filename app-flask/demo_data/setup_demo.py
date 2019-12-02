#!/usr/bin/env python3
from app import db

from models.user_model import UserModel
from models.session_model import SessionModel


primo_user = UserModel("primo_user", "primo@user.blah", "secret")
db.session.add(primo)

session1 = SessionModel()
session2 = SessionModel()
db.session.add(session1)

db.session.commit()
