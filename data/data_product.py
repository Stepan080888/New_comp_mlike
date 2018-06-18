from model.product import Product
from pymongo import MongoClient
import pymongo
import json

def create_test_data_for_test():
    client = MongoClient('192.168.12.203', 27018)
    db = client.shopdb
    product_list_from_db = db.products.find({})
    list_object_products_from_db = []
    for product in product_list_from_db:
        #file = json.load(i)
        #print("QQQQ:     ", product["_id"])
        product_id = product["_id"]
        product_name = product["name"]
        product_price = product["price"]
        product_quantity = round(product["totalQuantity"] / 15)
        list_object_products_from_db.append(Product(id=product_id, name=product_name, price=product_price, quantity=product_quantity))
    print(list_object_products_from_db)
    return list_object_products_from_db


a = create_test_data_for_test()[0:5]
print(a)