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
    result = db.execute(f"SELECT id, user_id, created, modified, focus, win, challenge, next_step FROM focus_session WHERE id={_id} AND user_id={user_id}")
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
    results = db.execute(f"SELECT id, user_id, created, modified, focus, win, challenge, next_step FROM focus_session WHERE user_id={user_id} ORDER BY created DESC")
    focus_sessions_data = results.fetchall()
    db.close()

    if focus_sessions_data:
      return [cls(*focus_session_data) for focus_session_data in focus_sessions_data]
    else:
      return None

  @classmethod
  def create_focus_session(cls, user_id, focus, win, challenge, next_step):
    created = datetime.now(timezone.utc).timestamp()
    modified = created
    db = sqlite3.connect('data.sqlite3')
    db.execute(f"INSERT INTO focus_session (user_id, created, modified, focus, win, challenge, next_step) VALUES (?, ?, ?, ?, ?, ?, ?)", (user_id, created, modified, focus, win, challenge, next_step))
    db.commit()
    db.close()

  @classmethod
  def update_focus_session(cls, focus_session_id, user_id, focus, win, challenge, next_step):
    focus_session = FocusModel.get_focus_session_by_id(focus_session_id, user_id)
    modified = datetime.now(timezone.utc).timestamp()
    db = sqlite3.connect('data.sqlite3')
    db.execute(f"UPDATE focus_session SET modified=?, focus=?, win=?, challenge=?, next_step=? WHERE id={focus_session_id} AND user_id={user_id}", (modified, focus, win, challenge, next_step))
    db.commit()
    db.close()
    return FocusModel.get_focus_session_by_id(focus_session_id, user_id)

  @classmethod
  def delete_focus_session(cls, focus_session_id, user_id):
    db = sqlite3.connect('data.sqlite3')
    db.execute(f"DELETE FROM focus_session WHERE id=? AND user_id=?", (focus_session_id, user_id))
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