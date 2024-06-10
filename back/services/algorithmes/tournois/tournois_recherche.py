from services.connexion.DatabaseService import DatabaseService


def rechercher_tournois_par_date(date: str):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    filtre = {"date": date}
    resultat = list(collection.find(filtre))
    db.seDeconnecter()
    return resultat


def rechercher_tournois_par_lieu(nom_lieu: str):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    filtre = {"lieu.nom": nom_lieu}
    resultat = list(collection.find(filtre))
    db.seDeconnecter()
    return resultat


def tournois_statut(statut):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    tournois = list(collection.find({"statut": statut}))
    return tournois

def trouver_tournoi_par_id(id_tournoi):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    tournoi = collection.find_one({"_id": id_tournoi}, {"_id": 0})
    db.seDeconnecter()
    return tournoi


def tout_les_tournois():
    db = DatabaseService()
    collection = db.get_collection("tournois")
    result = list(collection.find({}))
    db.seDeconnecter()
    return result


def rechercher_tournois_par_numero(numero: str):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    projection = {"_id": 0}
    filtre = {
        "joueurs.numeroInscription": numero
    }
    result = list(collection.find(filtre, projection))
    db.seDeconnecter()
    return result

def tout_les_matchs():
    db = DatabaseService()
    collection = db.get_collection("tournois")
    tous_les_matchs = []

    tous_les_tournois = collection.find({}, {"_id": 1, "nomTournoi": 1, "type": 1, "nature": 1, "matchs": 1})

    for tournoi in tous_les_tournois:
        tournoi_id = tournoi["_id"]
        nom_tournoi = tournoi["nomTournoi"]
        type_tournoi = tournoi["type"]
        nature_tournoi = tournoi["nature"]
        matchs_tournoi = tournoi.get("matchs", [])

        for match in matchs_tournoi:
            match["tournoi"] = {
                "id": tournoi_id,
                "nom": nom_tournoi,
                "type": type_tournoi,
                "nature": nature_tournoi
            }
            tous_les_matchs.append(match)

    db.seDeconnecter()
    return tous_les_matchs


