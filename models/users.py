import sqlite3
from flask_restful import reqparse, abort, Api, Resource
from flask_jwt import JWT, jwt_required, current_identity
from db import db

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(50))
    password = db.column(db.String(50))

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

    def json(self):
        return{'username':self.username, 'password':'password'}


    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def find_by_id(_id):
        return User.query.filter_by(id = _id).first()

    def add_user(self):
        db.session.add(self)
        db.session.commit()
