import sqlite3


def createtables():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    create_table_users = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)'
    cursor.execute(create_table_users)

    create_table_items = 'CREATE TABLE IF NOT EXISTS items (id INTEGER  PRIMARY KEY, name TEXT, price INTEGER)'
    cursor.execute(create_table_items)

    create_table_stores = 'CREATE TABLE IF NOT EXISTS stores (id INTEGER PRIMARY KEY, name TEXT)'
    cursor.execute(create_table_stores)

    connection.commit()
    connection.close()
