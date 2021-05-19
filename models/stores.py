import sqlite3
from flask_restful import reqparse, abort, Api, Resource
from flask_jwt import JWT, jwt_required, current_identity
from db import db

class Stores(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


    def __str__(self):
        return "Stores(id='%s')" % self.id

    def json(self):
        return{'name': self.name}

    @staticmethod
    def find_by_name(name):
        return Stores.query.filter_by(name=name).first()

    @staticmethod
    def find_by_id(_id):
        return Stores.query.filter_by(id=_id).first()

    def add_store(self):
        db.session.add(self)
        db.session.commit()

    def delete_store(self):
        db.session.delete(self)
        db.session.commit()