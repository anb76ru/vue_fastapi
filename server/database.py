from pymongo import MongoClient

connect_str = "mongodb+srv://anb76ru:pUR0g7uNNCYow2I9@cluster0.z9ddc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# connect_str = 'mongodb://localhost:27017/'


class Mongo:

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Mongo, cls).__new__(cls)

        return cls.instance

    def __init__(self):
        self.client = MongoClient(connect_str)
        self.db = self.client.get_database('mongo_vue_fastapi')

MongoDB = Mongo()
