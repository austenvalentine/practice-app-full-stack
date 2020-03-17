from smtplib import SMTP_SSL
from secrets import token_urlsafe
from app_config import app_config

def send_verify_email(recipient_email, recipient_name):
  username = app_config["smtp_username"]
  password = app_config["smtp_password"]
  server = app_config["smtp_server"]
  verify_uri = app_config["verify_uri"]
  ssl = app_config["smtp_ssl"]
  sender_email = app_config["smtp_sender_email"]
  sender_name = app_config["smtp_sender_name"]
  connection = SMTP_SSL(server, ssl)
  connection.login(username, password)


  token = token_urlsafe()
  part_boundary = token_urlsafe()

  message = f"""MIME-Version: 1.0
From: {sender_name} <{sender_email}>
To: {recipient_name} <{recipient_email}>
Subject: {sender_name} Registration
Content-Type: text/plain; charset="UTF-8"

Hello {recipient_name},

Please follow the URL and log in to complete your registration.

{verify_uri}?token={token}

Thank you,

{sender_name}
  """
  connection.sendmail(from_addr=sender_email, to_addrs=recipient_email, msg=message)

  return token