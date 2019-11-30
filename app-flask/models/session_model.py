from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SessionModel(db.Model):

    __tablename__="sessions"

    idkey = db.Column(db.Integer, primary_key=True )
    user_id = db.Column(db.Integer, db.ForeignKey('users.idkey'))
    date = db.Column(db.DateTime
    goal = db.Column(db.String(128))
    win = db.Column(db.String(128))
    difficulty = db.Column(db.String(128))
    plan = db.Column(db.String(128))

    def __init__(self, user_id=None, goal='', win='', difficulty='', plan=''):
        self.user_id = user_id
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