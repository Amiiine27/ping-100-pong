from services.connexion.DatabaseService import DatabaseService


def insertion_equipe(nom: str, joueurs: list[str, str]):
    db = DatabaseService()
    collection = db.get_collection("equipe")
    document = {
        "nom": nom,
        "joueurs": {
            "j1": joueurs[0],
            "j2": joueurs[1]
        }
    }
    collection.insert_one(document)
    db.seDeconnecter()

