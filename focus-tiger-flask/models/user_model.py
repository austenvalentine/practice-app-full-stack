from werkzeug.security import safe_str_cmp, generate_password_hash
from flask_restful import reqparse
from private_config import private_config
import psycopg2


class UserModel():
  connection_args = {
    "dbname":   private_config["pg_dbname"],
    "user":     private_config["pg_user"],
    "password": private_config["pg_password"],
    "host":     private_config["pg_host"],
    "port":     private_config["pg_port"]
  }

  def __init__(self, username=None, email=None, passhash=None, _id=None):
    self.id = _id
    self.passhash = passhash
    if username:
      self.username = username.lower()
    else:
      self.username = None
    if email:
      self.email = email.lower()
    else:
      self.email = None


  # database methods

  def __dbinsert(self, query, query_values=None, exception_callback=None):
    try:
      connection = psycopg2.connect(**UserModel.connection_args)
      cursor = connection.cursor()
      cursor.execute(query, query_values)
      connection.commit()
      connection.close()
      return True
    except:
      if exception_callback:
        exception_callback()
      else:
        print("UserModel.__dbinsert: INSERT FAILED")
      return False

  def __dbfetchone(self, query, query_values=None, exception_callback=None):
    try:
      connection = psycopg2.connect(**UserModel.connection_args)
      cursor = connection.cursor()
      cursor.execute(query, query_values)
      result = cursor.fetchone()
      connection.close()
      return result
    except:
      if exception_callback:
        exception_callback()
      else:
        print("UserModel.__dbfetchone: FETCHONE FAILED")
      return False


  # user methods

  def add(self):
    response = None
    if (self.exists()):
      return false
    response = self.__dbinsert(
      "INSERT INTO focus_user (username, email, passhash) VALUES (%s,%s,%s)",
      (self.username, self.email, self.passhash)
    )
    if response:
      return True
    return False

  def exists(self):
    another_user_username = UserModel(self.username).get_by_username()
    another_user_email = UserModel(self.email).get_by_email()
    if another_user_username or another_user_email:
      return True
    return False

  def get_by_id(self):
    requested_user = self.__dbfetchone('SELECT id, username, email, passhash FROM focus_user WHERE id=%s', [self.id])
    if requested_user:
      self.username = requested_user[1]
      self.email = requested_user[2]
      self.passhash = requested_user[3]
      return self
    return None

  def get_by_username(self):
    requested_user = self.__dbfetchone('SELECT id, username, email, passhash FROM focus_user WHERE username=%s',[self.username])
    if requested_user:
      self.id = requested_user[0]
      self.email = requested_user[2]
      self.passhash = requested_user[3]
      return self
    return None

  def get_by_email(self):
    requested_user = self.__dbfetchone('SELECT id, username, email, passhash FROM focus_user WHERE email=%s',[self.email])
    if requested_user:
      self.id = requested_user[0]
      self.username = requested_user[1]
      self.passhash = requested_user[3]
      return self
    return None
    
  def verify_password(self):
    password_hash = generate_password_hash(password)
    if (safe_str_cmp(password_hash, self.passhash)):
      return True
    return False


  def json(self):
    return {
      "username": self.username,
      "email": self.email
    }

