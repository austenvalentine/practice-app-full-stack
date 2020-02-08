from db import db
from datetime import datetime

class SessionModel(db.Model):
    __tablename__="sessions"

    idkey = db.Column(db.Integer, primary_key=True )
    user_id = db.Column(db.Integer, db.ForeignKey('users.idkey'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    goal = db.Column(db.String(64), default="Staying focused is the goal.")
    win = db.Column(db.String(64), default="I'm committed to regular study.")
    difficulty = db.Column(db.String(64), default="No difficulties stood out.")
    plan = db.Column(db.String(64), default="I'm open to suggestions for improvement.")

    def __init__(self, user, goal='', win='', difficulty='', plan=''):
        self.user_id = user.idkey
        self.goal = goal
        self.win = win
        self.difficulty = difficulty
        self.plan = plan
    
    def json(self):
        return { 
            "idkey": self.idkey,
            "user_id": self.user_id,
            "date": self.date.timestamp()

        }

    @classmethod
    def find_by_id(cls, idkey):
        return cls.query.filter_by(idkey=idkey).first()

    @classmethod
    def find_by_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


