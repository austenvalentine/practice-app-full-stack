import sqlite3
from datetime import datetime, timezone

class FocusModel():
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
  def get_focus_session_by_id(cls, _id, user_id):
    focus_session_data = None
    
    db = sqlite3.connect('data.sqlite3')
    result = db.execute("SELECT id, user_id, created, modified, focus, win, challenge, next_step FROM focus_session WHERE id=? AND user_id=?", (_id, user_id))
    focus_session_data = result.fetchone()
    db.close()

    if focus_session_data:
      return cls(*focus_session_data)
    else:
      return None

  @classmethod
  def get_focus_sessions_by_user_id(cls, user_id):
    focus_sessions = []

    db = sqlite3.connect('data.sqlite3')
    results = db.execute("SELECT id, user_id, created, modified, focus, win, challenge, next_step FROM focus_session WHERE user_id=? ORDER BY created DESC, id DESC", (str(user_id)))
    focus_sessions_data = results.fetchall()
    db.close()

    if focus_sessions_data:
      return [cls(*focus_session_data) for focus_session_data in focus_sessions_data]
    else:
      return None

  @classmethod
  def create_focus_session(cls, user_id, focus, win, challenge, next_step):
    try:
      db = sqlite3.connect('data.sqlite3')
      db.execute("INSERT INTO focus_session (user_id, created, modified, focus, win, challenge, next_step) VALUES (?, strftime('%s', 'now'), strftime('%s', 'now'), ?, ?, ?, ?)", (user_id, focus, win, challenge, next_step))
      db.commit()
      db.close()
    except sqlite3.IntegrityError:
      db.close()
      return False
    
    return True

  @classmethod
  def update_focus_session(cls, focus_session_id, user_id, focus, win, challenge, next_step):
    focus_session = FocusModel.get_focus_session_by_id(focus_session_id, user_id)
    if not cls.get_focus_session_by_id(focus_session_id, user_id):
      return False
    try:
      db = sqlite3.connect('data.sqlite3')
      db.execute(f"UPDATE focus_session SET modified=strftime('%s', 'now'), focus=?, win=?, challenge=?, next_step=? WHERE id=? AND user_id=?", (focus, win, challenge, next_step, focus_session_id, user_id))
      db.commit()
      db.close()
      return FocusModel.get_focus_session_by_id(focus_session_id, user_id)
    except sqlite3.IntegrityError:
      return False

  @classmethod
  def delete_focus_session(cls, focus_session_id, user_id):
    db = sqlite3.connect('data.sqlite3')
    db.execute("DELETE FROM focus_session WHERE id=? AND user_id=?", (focus_session_id, user_id))
    db.commit()
    db.close()

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