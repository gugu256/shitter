from tinydb import TinyDB, Query

users = TinyDB("users.json")
users_table = users.table('users')
