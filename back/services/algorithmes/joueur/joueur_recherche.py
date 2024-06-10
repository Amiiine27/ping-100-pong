from services.connexion.DatabaseService import DatabaseService


def recherche_joueur(objet_de_recherche: str):
    db = DatabaseService()
    collections = db.get_collection("joueur")
    filtre = {
        "$or": [
            {"nom": objet_de_recherche},
            {"prenom": objet_de_recherche}
        ]
    }
    projection = {"nom": 1, "prenom": 1, "_id": 0}
    result = list(collections.find(filtre, projection))
    db.seDeconnecter()
    return result


def tout_les_joueurs():
    db = DatabaseService()
    collections = db.get_collection("joueur")
    projection = {"_id": 0}
    result = list(collections.find({}, projection))
    db.seDeconnecter()
    return result


def recherche_par_numero(numero):
    db = DatabaseService()
    collections = db.get_collection("joueur")
    projection = {"_id": 0}
    filtre = {
      "numeroInscription": numero
    }
    result = list(collections.find(filtre, projection))
    db.seDeconnecter()
    return result

