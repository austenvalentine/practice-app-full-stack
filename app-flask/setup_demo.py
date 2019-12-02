#!/usr/bin/env python3
from app import app, db

from models.user_model import UserModel
from models.session_model import SessionModel

app.app_context().push()
db.init_app(app)
db.drop_all()
db.create_all()

primo_user = UserModel("primo_user", "primo@user.blah", "secret")
db.session.add(primo_user)
db.session.commit()

session1 = SessionModel(primo_user, 'shred', 'played fast', 'too slow', 'play faster')
db.session.add(session1)
session2 = SessionModel(primo_user, 'swing', 'swung hard', 'too soft', 'swing harder')
db.session.add(session2)
session3 = SessionModel(primo_user)

db.session.commit()
