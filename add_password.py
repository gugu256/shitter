import hashlib
from tinydb import TinyDB
db = TinyDB("certifications.json")
u = input("USR: ")
p = input("PAS: ")
h_p = hashlib.new("SHA512")
h_p.update(p.encode("utf-8"))
db.insert({"user":u, "password":h_p.hexdigest()})
print(h_p.hexdigest())