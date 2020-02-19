#!/usr/bin/env python3
from app_config import app_config
import sqlite3

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

db = sqlite3.connect('data.sqlite3')
db.execute("CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, password TEXT)")

for user in users:
  db.execute("INSERT INTO user (username, email, password) VALUES (?, ?, ?)", [user["username"], user["email"], user["password"]])



db.commit()
db.close()