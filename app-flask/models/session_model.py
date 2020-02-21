import sqlite3
from datetime import datetime, timezone

class SessionModel():
  def __init__(self, _id, user_id, created, modified, focus, win, challenge, next_step):
    self.id = _id
    self.user_id = user_id
    self.created = created
    self.modified = modified
    self.focus = focus
    self.win = win
    self.challenge = challenge
    self.next_step = next_step

  @classmethod
  def get_session_by_id(cls, _id, user_id):
    session_data = None
    
    db = sqlite3.connect('data.sqlite3')
    result = db.execute(f"SELECT id, user_id, created, modified, focus, win, challenge, next_step FROM session WHERE id={_id} AND user_id={user_id}")
    session_data = result.fetchone()
    db.close()

    if session_data:
      session = cls(
        *session_data
      )
      return session
    else:
      return None

  @classmethod
  def get_sessions_by_user_id(cls, user_id):
    sessions = []

    db = sqlite3.connect('data.sqlite3')
    results = db.execute(f"SELECT id, user_id, created, modified, focus, win, challenge, next_step FROM session WHERE user_id={user_id}")
    sessions_data = results.fetchall()
    db.close()

    if sessions_data:
      return [cls(*session) for session in sessions_data]
    else:
      return None

  def json(self):
    return ({
      "id": self.id,
      "user_id": self.user_id,
      "created": self.created,
      "modified": self.modified,
      "focus": self.focus,
      "win": self.win,
      "challenge": self.challenge,
      "next_step": self.next_step
    })