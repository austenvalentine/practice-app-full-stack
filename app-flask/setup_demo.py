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

session1 = SessionModel(primo_user.idkey, 'shred', 'played fast', 'too slow', 'play faster')
db.session.add(session1)
session2 = SessionModel(primo_user.idkey, 'swing', 'swung hard', 'too soft', 'swing harder')
db.session.add(session2)

db.session.commit()
