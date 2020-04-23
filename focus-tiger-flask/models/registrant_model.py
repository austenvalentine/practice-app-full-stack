from werkzeug.security import safe_str_cmp, generate_password_hash
from private_config import private_config
from flask_restful import reqparse
import psycopg2


class RegistrantModel():
  connection_args = {
    "dbname":   private_config["pg_dbname"],
    "user":     private_config["pg_user"],
    "password": private_config["pg_password"],
    "host":     private_config["pg_host"],
    "port":     private_config["pg_port"]
  }

  def __init__(self, username=None, email=None, password=None, passhash=None, token=None, _id=None):
    self.id = _id
    self.token = token
    if username:
      self.username = username.lower()
    else:
      self.username = None
    if email:
      self.email = email.lower()
    else:
      self.email = None
    # new users pass in password
    # db retrievals pass in _id and passhash
    if password:
      self.passhash = generate_password_hash(password)
    elif _id and passhash:
      self.passhash = passhash
    else:
      password = None

  
  # database methods

  def __dbinsert(self, query, query_values=None, exception_callback=None):
    try:
      connection = psycopg2.connect(**RegistrantModel.connection_args)
      cursor = connection.cursor()
      cursor.execute(query, query_values)
      connection.commit()
      connection.close()
      return True
    except:
      if exception_callback:
        exception_callback()
      else:
        print("RegistrantModel.__dbinsert: INSERT FAILED")
      return False

  def __dbdelete(self, query, query_values, exception_callback=None):
    try:
      connection = psycopg2.connect(**RegistrantModel.connection_args)
      cursor = connection.cursor()
      cursor.execute(query, query_values)
      connection.commit()
      connection.close()
      return True
    except:
      if exception_callback:
        exception_callback()
      else:
        print("RegistrantModel.__dbdelete: DELETE FAILED")
      return False

  def __dbfetchone(self, query, query_values=None, exception_callback=None):
    try:
      result = None
      connection = psycopg2.connect(**RegistrantModel.connection_args)
      cursor = connection.cursor()
      cursor.execute(query, query_values)
      result = cursor.fetchone()
      connection.close()
      return result
    except:
      if exception_callback:
        exception_callback()
      else:
        print("RegistrantModel.__dbfetchone: FETCHONE FAILED")
      return False


  # user methods

  def add(self):
    response = None
    if (self.exists()):
      self.__dbdelete("DELETE FROM registrant WHERE email=%s", [self.email])
    response = self.__dbinsert(
      """INSERT INTO registrant (username, email, passhash, token) VALUES (%s,%s,%s,%s)""",
      (self.username, self.email, self.passhash, self.token)
    )

    if response:
      return True
    return False

  def exists(self):
    another_registrant = RegistrantModel(email=self.email).get_by_email()
    if another_registrant:
      return True
    return False

  def get_by_email(self):
    requested_registrant = self.__dbfetchone("""SELECT id, username, email, passhash, token FROM registrant WHERE email=%s""",[self.email])
    if requested_registrant:
      self.id = requested_registrant[0]
      self.username = requested_registrant[1]
      self.passhash = requested_registrant[3]
      self.token = requested_registrant[4]
      return self
    return None

  def get_by_token(self):
    requested_registrant = self.__dbfetchone(
      """SELECT id, username, email, passhash, token FROM registrant WHERE token=%s""",
      [self.token])
    if requested_registrant:
      self.id = requested_registrant[0]
      self.username = requested_registrant[1]
      self.email = requested_registrant[2]
      self.passhash = requested_registrant[3]
      return self

  def delete(self):
    self.__dbdelete("DELETE FROM registrant WHERE email=%s", [self.email])
    
  def verify_password(self, password):
    password_hash = generate_password_hash(password)
    if (safe_str_cmp(password_hash, self.passhash)):
      return True
    return False

  def json(self):
    return {
      "username": self.username,
      "email": self.email
    }

