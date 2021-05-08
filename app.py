from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource

from flask import Flask
from flask_jwt import JWT
from security import authenticate, identity
from resources.items import Item, ItemList
from resources.users import UserRegister
from table import createtables
from db import db


app = Flask(__name__)
api = Api(app)
db.init_app(app)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'super-secret'

createtables()

jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/items/<name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(debug=True)