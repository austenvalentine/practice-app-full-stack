from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    idkey = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    hash_pw = db.Column(db.String(32))

    def __init__(self, username='', email='', hash_pw=''):
        self.username = username
        self.email = email
        self.hash_pw = hash_pw

    def json(self):
        return { 
            "idkey": self.idkey,
            "username": self.username,
            "email": self.email
        }

    @classmethod
    def find_by_id(cls, user):
        return cls.query.filter_by(idkey=idkey).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def update_email(self, email):
        if UserModel.find_by_email(email):
            return None
        self.email = email
        db.session.commit()

    def update_username(self, username):
        if UserModel.find_by_username(username):
            return None
        self.username = username
        db.session.commit()

    def update_pw(self, pw):
        self.hash_pw = pw   
        db.session.commit()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

