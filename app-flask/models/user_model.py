from werkzeug.security import safe_str_cmp
import sqlite3

class UserModel():
  def __init__(self, _id, username, email, password, ):
    self.id = _id
    self.username = username
    self.email = email
    self.password = password

  @classmethod
  def get_user_by_id(cls, _id):
    db = sqlite3.connect('data.sqlite3');
    result = db.execute(f'SELECT id, username, email, password FROM user WHERE id={_id}')
    requested_user = result.fetchone()
    db.close()
    return cls(
      _id=requested_user[0],
      username=requested_user[1],
      email=requested_user[2],
      password=requested_user[3]
    )

  @classmethod
  def get_by_username(cls, username):
    db = sqlite3.connect('data.sqlite3')
    result = db.execute(f'SELECT * FROM user WHERE username="{username}"')
    requested_user = result.fetchone()
    db.close()
    return cls(
      _id=requested_user[0],
      username=requested_user[1],
      email=requested_user[2],
      password=requested_user[3]
    )
    
  def verify_password(self, password):
    if (safe_str_cmp(password, self.password)):
      return True
    return False


  def json(self):
    return {
      "username": self.username,
      "email": self.email
    }

