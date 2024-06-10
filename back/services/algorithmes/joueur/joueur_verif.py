from services.connexion.DatabaseService import DatabaseService


def joueur_deja_inscrit(numero_inscription):
    db = DatabaseService()
    collection = db.get_collection("tournois")

    tournois = collection.find({"statut": True})

    for tournoi in tournois:
        joueurs_actuels = tournoi.get("joueurs", [])

        for joueur in joueurs_actuels:
            if joueur["numeroInscription"] == numero_inscription:
                return True

    return False


def joueur_existe(nom, prenom, numero_inscription=None, age=None, genre=None):
    db = DatabaseService()
    collection = db.get_collection("joueur")

    joueur_query = {
        "nom": nom,
        "prenom": prenom
    }

    if numero_inscription:
        joueur_query["numeroInscription"] = numero_inscription

    if age is not None:
        joueur_query["age"] = age

    if genre:
        joueur_query["genre"] = genre

    joueur = collection.find_one(joueur_query)

    return joueur is not None
