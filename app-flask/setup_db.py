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
db.execute("CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, password TEXT,CONSTRAINT unique_username UNIQUE (username))")

db.execute("CREATE TABLE focus_session (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, created REAL, modified REAL, focus TEXT, win TEXT, challenge TEXT, next_step TEXT)")

for user in users:
  db.execute("INSERT INTO user (username, email, password) VALUES (?, ?, ?)",
  (user["username"], user["email"], user["password"]))

for focus_session in focus_sessions:
  db.execute("INSERT INTO focus_session (user_id, created, modified, focus, win, challenge, next_step) VALUES (?, ?, ?, ?, ?, ?, ?)",
  (focus_session["user_id"], focus_session["created"], focus_session["modified"], focus_session["focus"], focus_session["win"], focus_session["challenge"], focus_session["next_step"]))

db.commit()
db.close()