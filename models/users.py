import sqlite3
from flask_restful import reqparse, abort, Api, Resource
from flask_jwt import JWT, jwt_required, current_identity
from db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))


    def __str__(self):
        return "User(id='%s')" % self.id

    def json(self):
        return{'username': self.username, 'password': self.password}


    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def find_by_id(_id):
        return User.query.filter_by(id=_id).first()

    def add_user(self):
        db.session.add(self)
        db.session.commit()
