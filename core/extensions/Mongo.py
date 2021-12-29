from pymongo import MongoClient


class MongoConnector:
    def __init__(self, db_uri, db_name) -> None:
        self.client = MongoClient(db_uri)[db_name]

    def get_collection(self, name):
        return self.client[name]
