import sqlite3
from flask_restful import reqparse, abort, Api, Resource
from flask_jwt import JWT, jwt_required, current_identity
from db import db


class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    store = db.Column(db.String(50))

    def __str__(self):
        return "Items(id='%s')" % self.id

    def json(self):
        return{'name': self.name, 'price': self.price, 'store': self.store}

    @staticmethod
    def find_by_name(name):
        return Items.query.filter_by(name=name).first()

    @staticmethod
    def find_by_id(_id):
        return Items.query.filter_by(id=_id).first()

    def add_item(self):
        db.session.add(self)
        db.session.commit()

    def delete_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

    @staticmethod
    def get_all():
        return Items.query.all()

