from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.session_model import SessionModel
from models.user_model import UserModel




class Session(Resource):
    @jwt_required
    def get(self):
        _id = get_jwt_identity()
        return UserModel.find_by_id(_id).json()

    @jwt_required
    def post(self):
        return {"message": "you have access"}
    
    def delete(self):
        pass

    def put(self):
        pass

class Sessions(Resource):
    _session_parser = reqparse.RequestParser()
    def get(self, userid):
        return [session.json() for session in SessionModel.find_by_user(userid)]