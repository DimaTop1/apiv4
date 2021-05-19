import sqlite3
from flask_restful import reqparse, abort, Api, Resource
from flask_jwt import JWT, jwt_required, current_identity
from models.stores import Stores

class Store(Resource):
    @jwt_required()
    def get(self, name):
        if Stores.find_by_name(name):
            store = Stores.find_by_name(name)
            return store.json()
        else:
            return f"item {name} doesn`t exist"


    @jwt_required()
    def delete(self, name):
        if Stores.find_by_name(name):
            store = Stoores.find_by_name(name)
            store.delete_item()
            return '', 204
        else:
            return f"item {name} doesn`t exist"



    @jwt_required()
    def post(self, name):
        if Stores.find_by_name(name):
            return f"item {name} already exists"
        argsfull = {'name':name}
        item = Items(**argsfull)
        item.add_item()
        return item.json(), 201
