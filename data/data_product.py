from model.product import Product
from pymongo import MongoClient
import pymongo
import json


#def create_test_data_for_test(number_embeded_lists):
    #client = MongoClient('192.168.12.203', 27018)

def create_test_data_for_test(number_embeded_lists):
    client = MongoClient('192.168.12.203', 27018)
    db = client.shopdb
    product_list_from_db = db.products.find({})
    list_in_list = []
    list_object_products_from_db = []
    for i in range(number_embeded_lists):
        for product in product_list_from_db:
            product_id = product["_id"]
            product_name = product["name"]
            product_price = product["price"]
            product_quantity = round(product["totalQuantity"] / 15)
            list_object_products_from_db.append(Product(id=product_id, name=product_name, price=product_price, quantity=product_quantity))
        list_in_list.append(list_object_products_from_db[0:i+1])
    #print(list_object_products_from_db)
    return list_in_list



product_lists = create_test_data_for_test(2)

a = create_test_data_for_test(3)[0:5]
print(a)

