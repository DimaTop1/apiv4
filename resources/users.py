import sqlite3
from flask_restful import reqparse, abort, Api, Resource
from flask_jwt import JWT, jwt_required, current_identity
from models.users import User

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help="Username cannot be blank!")
        parser.add_argument('password', help="Password cannot be blank!")
        args = parser.parse_args()
        if User.find_by_username(args['username']):
            return f"user {args['username']} already exists"
        user = User(**user)
        user.add_user()

        return user.json(), 400