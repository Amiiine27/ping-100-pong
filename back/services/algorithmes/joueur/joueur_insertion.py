from services.connexion.DatabaseService import DatabaseService


def insertion_joueur(genre: str, nom: str, prenom: str, age: int, courriel: str, telephone: str, adresse: str, codePostale: int, ville: str, pays: str, licence: str, classement: int):
    db = DatabaseService()
    collection = db.get_collection("joueur")
    document = {
        "genre": genre,
        "nom": nom,
        "prenom": prenom,
        "age": age,
        "courriel": courriel,
        "telephone": telephone,
        "adresse": adresse,
        "codePostale": codePostale,
        "ville": ville,
        "pays": pays,
        "licence": licence,
        "classement": classement,
    }
    result = collection.insert_one(document).inserted_id

    # Extraction des 8 derniers caractères de l'ObjectId
    objectid_last_8_chars = str(result)[-8:]
    print(objectid_last_8_chars)
    filter = {"_id": result}
    update = {"$set": {"numeroInscription": objectid_last_8_chars}}
    collection.update_one(filter, update)
    db.seDeconnecter()
    return {"numeroInscription": objectid_last_8_chars}


