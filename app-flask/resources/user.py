from flask_restful import Resource
class login(Resource):
  def get(self):
    return {"message": "Hello World!"}, 200