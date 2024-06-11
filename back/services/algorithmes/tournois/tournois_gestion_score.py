from services.algorithmes.tournois import tournois_modification
from services.connexion.DatabaseService import DatabaseService
def inserer_vainqueur_tournois_simple(id_tournoi):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    tournoi = collection.find_one({"_id": id_tournoi})

    if tournoi:
        matches = tournoi.get("matchs", [])
        for match in matches:
            adversaire1 = match["match"]["adversaire1"]
            adversaire2 = match["match"]["adversaire2"]
            score_adversaire1 = match["match"]["score"]["adversaire1"]
            score_adversaire2 = match["match"]["score"]["adversaire2"]

            if score_adversaire1 > score_adversaire2:
                vainqueur_nom = adversaire1["nom"] + " " + adversaire1["prenom"]
            elif score_adversaire1 < score_adversaire2:
                vainqueur_nom = adversaire2["nom"] + " " + adversaire2["prenom"]
            else:
                vainqueur_nom = "match_nul"

            filtre = {"_id": id_tournoi, "matchs.match": match["match"]}
            mise_a_jour = {"$set": {"matchs.$.vainqueur": vainqueur_nom}}
            collection.update_one(filtre, mise_a_jour)

    db.seDeconnecter()

def inserer_vainqueur_tournois_double(id_tournoi):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    tournoi = collection.find_one({"_id": id_tournoi})

    if tournoi:
        matches = tournoi.get("matchs", [])
        for match in matches:
            adversaire1 = match["match"]["adversaire1"]
            adversaire2 = match["match"]["adversaire2"]
            score_adversaire1 = match["match"]["score"]["adversaire1"]
            score_adversaire2 = match["match"]["score"]["adversaire2"]

            vainqueur_nom = ""
            if score_adversaire1 > score_adversaire2:
                vainqueur_nom = f"{adversaire1[0]['nom']} {adversaire1[0]['prenom']} et {adversaire1[1]['nom']} {adversaire1[1]['prenom']}"
            elif score_adversaire1 < score_adversaire2:
                vainqueur_nom = f"{adversaire2[0]['nom']} {adversaire2[0]['prenom']} et {adversaire2[1]['nom']} {adversaire2[1]['prenom']}"
            else:
                vainqueur_nom = "match_nul"

            filtre = {"_id": id_tournoi, "matchs.match": match["match"]}
            mise_a_jour = {"$set": {"matchs.$.vainqueur": vainqueur_nom}}
            collection.update_one(filtre, mise_a_jour)

    db.seDeconnecter()



def initialiser_scores(id_tournoi, matches):
    for match in matches:
        match["match"]["score"] = {
            "adversaire1": 0,
            "adversaire2": 0
        }
        match["vainqueur"] = ""
    tournois_modification.modifier_score_tournois(id_tournoi, matches)

