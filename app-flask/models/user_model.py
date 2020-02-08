from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    idkey = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    hash_pw = db.Column(db.String(32))

    def __init__(self, username='', hash_pw=''):
        self.username = username
        self.hash_pw = hash_pw

    def json(self):
        return { 
            "idkey": self.idkey,
            "username": self.username
        }

    @classmethod
    def find_by_id(cls, idkey):
        return cls.query.filter_by(idkey=idkey).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def update_username(self, username):
        if UserModel.find_by_username(username):
            return None
        self.username = username
        db.session.commit()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

