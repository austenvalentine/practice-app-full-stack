#!/usr/bin/env python3
from app_config import app_config
from datetime import datetime, timezone
import sqlite3

timestamp = datetime.now(timezone.utc).timestamp()

users = [
  { "username": "admin",
    "email": "admin@focusjournal.ca",
    "password": app_config["admin_pass"]
  },
  { 
    "username": "guest",
    "email" : "guest@focusjournal.ca",
    "password": "guest"
  }
]

focus_sessions = [
  { "user_id" : 1,
    "created" : timestamp - 500000,
    "modified" : timestamp - 400000,
    "focus" : "swing",
    "win" : "swung",
    "challenge" : "swinging harder",
    "next_step" : "swing harder"
  },
  { "user_id" : 2,
    "created" : timestamp - 350000,
    "modified" : timestamp - 250000,
    "focus" : "groove",
    "win" : "grooved",
    "challenge" : "grooving deeper",
    "next_step" : "groove deeper"
  },
  { 
    "user_id" : 2,
    "created" : timestamp,
    "modified" :  timestamp + 250000,
    "focus" : "shred",
    "win" : "shredded",
    "challenge" : "shredding faster",
    "next_step" : "shred faster"
  },
  { 
    "user_id" : 1,
    "created" : timestamp + 350000,
    "modified" :  timestamp + 400000,
    "focus" : "polka",
    "win" : "polkad",
    "challenge" : "polkaing harder",
    "next_step" : "polka harder"
  }
]

db = sqlite3.connect('data.sqlite3')
db.execute("""
  CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    active INTEGER NOT NULL,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT,
    CHECK(
      active >= 0 AND
      active <=1 AND
      length(username) < 32 AND
      length(email) < 32 AND
      length(password) < 100
    )
  )
""")

db.execute("""
  CREATE TABLE focus_session (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    created INTEGER NOT NULL,
    modified INTEGER NOT NULL,
    focus TEXT NOT NULL,
    win TEXT NOT NULL,
    challenge TEXT NOT NULL,
    next_step TEXT NOT NULL
  CHECK(
    length(focus) < 70 AND
    length(win) < 70 AND
    length(challenge) < 70 AND
    length(next_step) < 70
  )
)
""")

db.execute("""
  CREATE TABLE registrant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created INTEGER,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    CONSTRAINT unique_username UNIQUE (username),
    CHECK(
      length(username) < 32 AND
      length(email) < 32 AND
      length(password) < 100
    )
  )
""")

for user in users:
  db.execute("INSERT INTO user (username, email, password) VALUES (?, ?, ?)",
  (user["username"], user["email"], user["password"]))

for focus_session in focus_sessions:
  db.execute("INSERT INTO focus_session (user_id, created, modified, focus, win, challenge, next_step) VALUES (?, strftime('%s', 'now'), strftime('%s', 'now'), ?, ?, ?, ?)",
  (focus_session["user_id"], focus_session["focus"], focus_session["win"], focus_session["challenge"], focus_session["next_step"]))

db.commit()
db.close()