import psycopg2
from private_config import connection_args
from datetime import datetime, timezone
import json

class FocusModel():
  def __init__(self, _id=None, user_id=None, created=None, modified=None, focus=None, win=None, challenge=None, next_step=None):
    self.id = _id
    self.user_id = user_id
    self.created = created
    self.modified = modified
    self.focus = focus
    self.win = win
    self.challenge = challenge
    self.next_step = next_step


  # database methods

  def __dbfetchone(self, query, query_values, exception_callback=None):
    try:
      connection = psycopg2.connect(**connection_args)
      cursor = connection.cursor()
      cursor.execute(query, query_values)
      result = cursor.fetchone()
      connection.close()
      return result
    except:
      if exception_callback:
        exception_callback()
      else:
        print("FocusModel.__dbfetchone: FETCHONE FAILED")
      return False

  def __dbfetchall(self, query, query_values, exception_callback=None):
    try:
      connection = psycopg2.connect(**connection_args)
      cursor = connection.cursor()
      cursor.execute(query, query_values)
      results = cursor.fetchall()
      connection.close()
      return [FocusModel(*result) for result in results]
    except:
      if exception_callback:
        exception_callback()
      else:
        print("FocusModel.__dbfetchall: FETCHALL FAILED")
      return False

  def __dbdelete(self, query, query_values, exception_callback=None):
    try:
      connection = psycopg2.connect(**connection_args)
      cursor = connection.cursor()
      cursor.execute(query, query_values)
      connection.commit()
      connection.close()
      return True
    except:
      if exception_callback:
        exception_callback()
      else:
        print("FocusModel.__dbdelete: DELETE FAILED")
      return False

  def __dbinsert(self, query, query_values, exception_callback=None):
    try:
      connection = psycopg2.connect(**connection_args)
      cursor = connection.cursor()
      feedback = cursor.execute(query, query_values)
      connection.commit()
      connection.close()
      return True
    except:
      if exception_callback:
        exception_callback()
      else:
        print("FocusModel.__dbinsert: INSERT FAILED")
      return False

  def __dbupdate(self, query, query_values, exception_callback=None):
    try:
      connection = psycopg2.connect(**connection_args)
      cursor = connection.cursor()
      feedback = cursor.execute(query, query_values)
      connection.commit()
      connection.close()
      return True
    except:
      if exception_callback:
        exception_callback()
      else:
        print("FocusModel.__dbinsert: UPDATE FAILED")
      return False

  # focus session methods

  def get_by_id(self):
    result = self.__dbfetchone(
      "SELECT id, user_id, created, modified, focus, win, challenge, next_step FROM focus_session WHERE id=%s AND user_id=%s",
      (self.id, self.user_id))
    if result:
      self.created    = result[2]
      self.modified   = result[3]
      self.focus      = result[4]
      self.win        = result[5]
      self.challenge  = result[6]
      self.next_step  = result[7]
      return True
    else:
      return False

  def get_all_by_user_id(self):
    results = self.__dbfetchall("SELECT id, user_id, created, modified, focus, win, challenge, next_step FROM focus_session WHERE user_id=%s ORDER BY created DESC, id DESC", [self.user_id])
    return results

  def add(self):
    success = self.__dbinsert(
      "INSERT INTO focus_session (created, modified, user_id, focus, win, challenge, next_step) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, %s, %s, %s, %s, %s)",
      [self.user_id, self.focus, self.win, self.challenge, self.next_step]
    )
    return success
  
  def exists(self):
    existing_focus = FocusModel(_id=self.id, user_id=self.user_id).get_by_id()
    if existing_focus:
      return True
    return False
    
  def update(self):
    if not self.exists():
      return False
    return self.__dbupdate(
      "UPDATE focus_session SET modified=CURRENT_TIMESTAMP, focus=%s, win=%s, challenge=%s, next_step=%s WHERE id=%s AND user_id=%s",
      [self.focus, self.win, self.challenge, self.next_step, self.id, self.user_id])

  def delete(self):
    return self.__dbdelete("DELETE FROM focus_session WHERE id=%s AND user_id=%s", [self.id, self.user_id])

  def json(self):
    return ({
      "id": self.id,
      "user_id": self.user_id,
      "created": int(self.created.strftime('%s')) * 100,
      "modified": int(self.modified.strftime('%s')) * 100,
      "focus": self.focus,
      "win": self.win,
      "challenge": self.challenge,
      "next_step": self.next_step
    })