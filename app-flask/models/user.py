from flask import jsonify
import sqlite3

class UserModel():
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password

  @classmethod
  def get_user_by_id(cls, _id):
    db = sqlite3.connect('data.sqlite3');
    result = db.execute(f'SELECT * FROM user WHERE id={_id}')
    requested_user = result.fetchone()
    db.close()
    print(requested_user)
    return UserModel(
      requested_user[1],
      requested_user[2],
      requested_user[3]
      )

  def json(self):
    return {
      "username": self.username,
      "email": self.email, 
      "password": self.password
    }

