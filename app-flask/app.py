from flask import Flask
from flask_restful import Api
from resources.login import login

app = Flask(__name__)
api = Api()

api.add_resource(login)

if __name__=="__main__":
  app.run(port=5000, debug=True)