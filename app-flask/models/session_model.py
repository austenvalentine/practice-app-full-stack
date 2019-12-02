from db import db
import datetime

class SessionModel(db.Model):
    __tablename__="sessions"

    idkey = db.Column(db.Integer, primary_key=True )
    user_id = db.Column(db.Integer, db.ForeignKey('users.idkey'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
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
    
    @classmethod
    def find_by_id(self, idkey):
        return db.session.query.filter_by(idkey=idkey).first()

    @classmethod
    def find_by_user(self, user_id):
        return db.session.query.filter_by(user_id=user_id)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


