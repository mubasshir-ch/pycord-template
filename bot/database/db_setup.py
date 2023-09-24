from datetime import datetime
from pymongo import MongoClient

class Database:
    def __init__(self, uri):
        self.cluster = MongoClient(uri)
        self.db = self.cluster["db_name"]
        self.collection = self.db["collection_name"]