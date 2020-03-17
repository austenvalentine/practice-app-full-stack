from werkzeug.security import safe_str_cmp, generate_password_hash
from flask_restful import reqparse
import sqlite3



class UserModel():
  def __init__(self, _id, username, email, password, ):
    self.id = _id
    self.username = username.lower()
    self.email = email.lower()
    self.password = password

  @classmethod
  def add_user(cls, username, email, password):
    username_lower = username.lower()
    email_lower = email.lower()
    password_hash = generate_password_hash(password)
    if (cls.user_exists(username_lower, email_lower)):
      return false
    db = sqlite3.connect('data.sqlite3')
    db.execute("INSERT INTO user (username, email, password) VALUES (?,?,?)", (username_lower, email_lower, password_hash))
    db.close()

  @classmethod
  def user_exists(cls, username, email):
    username_lower = username.lower()
    email_lower = email.lower()
    if cls.get_user_by_username(username_lower) or cls.get_user_by_email(email_lower):
      return True
    return False

  @classmethod
  def get_user_by_id(cls, _id):
    db = sqlite3.connect('data.sqlite3');
    result = db.execute('SELECT id, username, email, password FROM user WHERE id=?', [_id])
    requested_user = result.fetchone()
    db.close()


    if requested_user == None:
      return None

    return cls(
      _id=requested_user[0],
      username=requested_user[1],
      email=requested_user[2],
      password=requested_user[3]
    )

  @classmethod
  def get_user_by_username(cls, username):
    username_lower = username.lower()
    db = sqlite3.connect('data.sqlite3')
    result = db.execute('SELECT * FROM user WHERE username=?',[username_lower])
    requested_user = result.fetchone()
    db.close()

    if requested_user == None:
      return None

    return cls(
      _id=requested_user[0],
      username=requested_user[1],
      email=requested_user[2],
      password=requested_user[3]
    )

  @classmethod
  def get_user_by_email(cls, email):
    email_lower = email.lower()
    db = sqlite3.connect('data.sqlite3')
    result = db.execute('SELECT * FROM user WHERE email=?', [email_lower])
    requested_user = result.fetchone()

    if requested_user == None:
      return None
      
    return cls(
      _id=requested_user[0],
      username=requested_user[1],
      email=requested_user[2],
      password=requested_user[3]
    )
    
  def verify_password(self, password):
    password_hash = generate_password_hash(password)
    if (safe_str_cmp(password_hash, self.password)):
      return True
    return False


  def json(self):
    return {
      "username": self.username,
      "email": self.email
    }

