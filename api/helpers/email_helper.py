from smtplib import SMTP_SSL
from secrets import token_urlsafe
from private_config import private_config

def send_verify_email(recipient_email, recipient_name):
  username = private_config["smtp_username"]
  password = private_config["smtp_password"]
  server = private_config["smtp_server"]
  verify_uri = private_config["verify_uri"]
  ssl = private_config["smtp_ssl"]
  sender_email = private_config["smtp_sender_email"]
  sender_name = private_config["smtp_sender_name"]
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

Please visit the URL and log in to complete your registration.

{verify_uri}/{token}

Thank you,

{sender_name}
  """
  connection.sendmail(from_addr=sender_email, to_addrs=recipient_email, msg=message)
  return token