from bson import ObjectId

from services.connexion.DatabaseService import DatabaseService


def modifier_joueur(id_joueur: str, document: str):
    db = DatabaseService()
    collection = db.get_collection("joueur")
    filtre = {"_id": ObjectId(id_joueur)}
    mise_a_jour = {"$set": document}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()

