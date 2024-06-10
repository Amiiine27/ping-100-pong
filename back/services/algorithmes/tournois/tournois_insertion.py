from services.connexion.DatabaseService import DatabaseService
from services.algorithmes.joueur.joueur_verif import joueur_deja_inscrit, joueur_existe
from services.algorithmes.joueur import joueur_match


def insertion_tournoi(id: str, nb_table: int, nom_tournoi: str, type: str, nature: str, place_disponible: int, statut: bool, date_ouverture: str, date_fermeture: str):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    document = {
        "_id": id,
        "nbTable": nb_table,
        "nomTournoi": nom_tournoi,
        "type": type,
        "nature": nature,
        "placeDisponible": place_disponible,
        "statut": statut,
        "dateOuverture": date_ouverture,
        "dateFermeture": date_fermeture,
        "joueurs": [],
        "matchs": []
    }
    collection.insert_one(document)
    db.seDeconnecter()

def insertion_joueur_tournoi(id_tournoi, numero_inscription, nom, prenom):
    result_messages = []

    if not joueur_existe(nom, prenom, numero_inscription=numero_inscription):
        result_messages.append("Le joueur n'existe pas dans la base de données des joueurs.")
        return result_messages

    if joueur_deja_inscrit(numero_inscription):
        result_messages.append("Le joueur est déjà inscrit à un tournoi.")
        return result_messages

    db = DatabaseService()
    collection = db.get_collection("tournois")

    joueur = {"numeroInscription": numero_inscription, "nom": nom, "prenom": prenom}

    tournoi = collection.find_one({"_id": id_tournoi})

    if not tournoi:
        result_messages.append("Tournoi non trouvé.")
        return result_messages

    joueurs_actuels = tournoi.get("joueurs", [])
    place_disponible = tournoi.get("placeDisponible", 0)

    if place_disponible <= 0:
        result_messages.append("Le tournoi est complet. Aucun joueur ne peut être ajouté.")
        return result_messages

    joueurs_actuels.append(joueur)
    place_disponible -= 1

    collection.update_one(
        {"_id": id_tournoi},
        {"$set": {"joueurs": joueurs_actuels, "placeDisponible": place_disponible}}
    )

    if place_disponible == 0:
        collection.update_one(
            {"_id": id_tournoi},
            {"$set": {"statut": False}}
        )
        result_messages.append("Nombre de participants atteint. Le tournoi est maintenant fermé.")
        joueur_match.gestion_matchs(id_tournoi)

    else:
        result_messages.append("Le joueur a été ajouté avec succès au tournoi.")

    return result_messages

def supprimer_joueur_tournoi(id_tournoi, numero_inscription):
    result_messages = []

    db = DatabaseService()
    collection = db.get_collection("tournois")

    tournoi = collection.find_one({"_id": id_tournoi})

    if not tournoi:
        result_messages.append("Tournoi non trouvé.")
        return result_messages

    joueurs_actuels = tournoi.get("joueurs", [])
    place_disponible = tournoi.get("placeDisponible", 0)

    joueur_supprime = False

    for joueur in joueurs_actuels:
        if joueur["numeroInscription"] == numero_inscription:
            joueurs_actuels.remove(joueur)
            place_disponible += 1
            joueur_supprime = True
            break

    if not joueur_supprime:
        result_messages.append("Le joueur n'est pas inscrit à ce tournoi.")
        return result_messages

    collection.update_one(
        {"_id": id_tournoi},
        {"$set": {"joueurs": joueurs_actuels, "placeDisponible": place_disponible}}
    )

    if place_disponible > 0:
        collection.update_one(
            {"_id": id_tournoi},
            {"$set": {"statut": True}}
        )
        result_messages.append("Le joueur a été supprimé avec succès du tournoi.")
    else:
        collection.update_one(
            {"_id": id_tournoi},
            {"$set": {"statut": False}}
        )
        result_messages.append("Nombre de participants atteint. Le tournoi est maintenant fermé.")

    return result_messages

