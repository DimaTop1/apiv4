from flask_restful import reqparse, abort, Api, Resource
from flask_jwt import JWT, jwt_required, current_identity
import sqlite3
import json
from json import JSONEncoder


class Items(object):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return "User(id='%s')" % self.id

    @staticmethod
    def find_by_name(name):
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        query = 'SELECT * FROM items WHERE name = ?'
        row = cur.execute(query, (name,))

        return list(row)

        con.close()


def abort_if_item_doesnt_exist(name):
    if not Items.find_by_name(name):
        abort(404, message="There's no such item in the shop {}".format(name))


def abort_if_item_already_exists(name):
    if Items.find_by_name(name):
        abort(404, message="Item {} already exists".format(name))



# item resource

class Item(Resource):
    @jwt_required()
    def get(self, name):
        abort_if_item_doesnt_exist(name)
        item = Items.find_by_name(name)
        return item




    @jwt_required()
    def delete(self, name):
        abort_if_item_doesnt_exist(name)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'DELETE FROM items WHERE name = ?'
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return '', 204

    @jwt_required()
    def post(self, name):
        abort_if_item_already_exists(name)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True, help="Price cannot be blank!")
        args = parser.parse_args()
        create_item = 'INSERT INTO items(id, name, price) VALUES (NULL, ?, ?)'
        item = (name, args['price'])
        cursor.execute(create_item, item)
        connection.commit()
        connection.close()
        return item, 201

    @jwt_required()
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True, help="Price cannot be blank!")
        args = parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        if Items.find_by_name(name):
            query = f" UPDATE items SET price = {args['price']} WHERE name = name"

            cursor.execute(query)
            connection.commit()
            return Items.find_by_name(name), 201
            connection.close()

        create_item = 'INSERT INTO items(id, name, price) VALUES (NULL, ?, ?)'
        item = (name, args['price'])
        cursor.execute(create_item, item)
        connection.commit()
        return item, 201
        connection.close()


# itemlist resource

class ItemList(Resource):

    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM items")

        rows = cursor.fetchall()
        return rows

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('items', type=dict, action='append', help="Name cannot be blank!")
        args = parser.parse_args()
        added = []
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        for i in range(len(args['items'])):
            if Items.find_by_name(args['items'][i]['name']):
                print("Item {} already exists".format(args['items'][i]['name']))
            else:
                create_item = 'INSERT INTO items(id, name, price) VALUES (NULL, ?, ?)'
                item = (args['items'][i]['name'], args['items'][i]['price'])
                cursor.execute(create_item, item)
                print("Item {} is added".format(args['items'][i]['name']))
                connection.commit()
                added.append(item)
        return added, 201
        connection.close()


