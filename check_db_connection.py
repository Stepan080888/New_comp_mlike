import pymongo
from pymongo import MongoClient
import datetime
import pprint


client = MongoClient('', 27018)
print("1", client)



db = client.shopdb
print("2", db)

collection = db.users
print("3 ", collection)

posts = db.posts
print("4 ", db.collection_names(include_system_collections=False))

postaldata_list_from_db = db.users.find_one({"nickname": "sily1234567890 www123456789"}, {"postalInfo": 1, "_id": 0})['postalInfo']
for i in postaldata_list_from_db:
    print("5: ", i)

#print("5 ", db.users.find_one({"nickname": "sily1234567890 www123456789"}, {"postalInfo": 1, "_id": 0})['postalInfo'])

#for  i in db.users.find({}):
#    print("6 ", i)
