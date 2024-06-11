# services/database.py
import os

from pymongo import MongoClient


class DatabaseService:

    def __init__(self):
        self.__uri = "mongodb://localhost:27017/"
        self.__dbname = "tennis"
        self.__client = MongoClient(self.__uri)[self.__dbname]

    def get_collection(self, collection_name):
        result = self.__client[collection_name]
        return result

    def seDeconnecter(self):
        self.__client.client.close()
