import pymongo


class Connexion:

    def __init__(self):  # initialisation de la connexion à la bd
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["pingpongtournament"]

    def fermer_client(self):
        self.client.close()