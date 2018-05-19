from pymongo import MongoClient

class DbFixture:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self. name = name
        self.connection_mongoclient = MongoClient('host', port)
        self.connection_db = self.connection_mongoclient.name

    def get_postaldata_from_db(self):
        try:
            self.connection_db.users.find_one({"nickname": "sily1234567890 www123456789"}, {"postalInfo": 1, "_id": 0})['postalInfo']
        finally:
            self.connection_mongoclient.close()


    def destroy(self):
        self.connection_mongoclient.close()