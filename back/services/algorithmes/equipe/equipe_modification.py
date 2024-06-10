from services.connexion.DatabaseService import DatabaseService


def modifier_nom_equipe(nom_equipe: str, nouveau_nom: str):
    db = DatabaseService()
    collection = db.get_collection("equipe")
    filtre = {"nom": nom_equipe}
    mise_a_jour = {"$set": {"nom": nouveau_nom}}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()


def modifier_joueur1_equipe(nom_equipe: str, nouveau_nom_joueur1: str):
    db = DatabaseService()
    collection = db.get_collection("equipe")
    filtre = {"nom": nom_equipe}
    mise_a_jour = {"$set": {"joueurs.j1": nouveau_nom_joueur1}}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()


def modifier_joueur2_equipe(nom_equipe: str, nouveau_nom_joueur2: str):
    db = DatabaseService()
    collection = db.get_collection("equipe")
    filtre = {"nom": nom_equipe}
    mise_a_jour = {"$set": {"joueurs.j2": nouveau_nom_joueur2}}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()


def modifier_equipe(nom_equipe: str, nouveau_nom: str, nouveau_nom_joueur1: str, nouveau_nom_joueur2: str):
    db = DatabaseService()
    collection = db.get_collection("equipe")
    filtre = {"nom": nom_equipe}
    mise_a_jour = {
        "$set": {
            "nom": nouveau_nom,
            "joueurs.j1": nouveau_nom_joueur1,
            "joueurs.j2": nouveau_nom_joueur2
        }
    }
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()

