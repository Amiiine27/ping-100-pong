from AppClasses.Connexion import Connexion


class Joueur(Connexion):
    _next_id = 0

    def __init__(self):
        Connexion.__init__(self)

    def inserer_joueur(self, prenom: str, nom: str, date_naissance: str, sexe: str, pseudo: str):
        """Insère un joueur avec tous les attributs entrés, ssi un joueur avec le même prénom,
         le même nom et la même date de naissance n'existe pas"""
        if prenom is None or nom is None or date_naissance is None or sexe is None or pseudo is None:
            return "Veuillez fournir toutes les informations nécessaires pour insérer un joueur"

        coll = self.db.personnes
        if self.joueur_existe(pseudo):
            return "Ce joueur existe déjà, il n'a pas été inséré"
        else:
            coll.insert_one(
                {"prenom": prenom, "nom": nom, "date_naissance": date_naissance, "sexe": sexe,
                 "pseudo": pseudo, "victoires": 0, "defaites": 0, "parties_jouees": 0 })
            return "Ce joueur a été inséré ! "

    def inserer_les_joueurs(self, file):
        compteur_y = 0
        compteur_n = 0
        if file.filename.endswith('.csv'):
            try:
                with file.stream as csvfile:
                    for line in csvfile:
                        line = line.decode('utf-8').strip()
                        prenom, nom, date_naissance, sexe, pseudo = line.split(';')

                        retour = self.inserer_joueur(prenom, nom, date_naissance, sexe, pseudo)

                        if retour == "Ce joueur a été inséré ! ":
                            compteur_y += 1
                        else:
                            compteur_n += 1

                return f"{compteur_y} Joueurs ont pu être insérés sur {compteur_n + compteur_y}"
            except Exception as e:
                return f"Une erreur s'est produite : {e}"
        else:
            return f"{file.filename} n'est pas un fichier csv"

    def joueur_existe(self, pseudo: str):
        coll = self.db.personnes
        requete = coll.find_one({"pseudo": pseudo})
        if requete is not None:
            return True
        else:
            return False

    def supprimer_joueur_par_pseudo(self, pseudo: str):

        coll = self.db.personnes
        joueur = coll.find_one({"pseudo": pseudo})
        if joueur:
            coll.delete_one({"pseudo": pseudo})
            return " Ce joueur a été supprimé ! :)"
        else:
            return "Le joueur avec le pseudo donné n'existe pas dans la base de données."

    def modifier_joueur_par_pseudo(self, pseudo: str, nouveau_pseudo: str) -> str:
        coll = self.db.personnes
        joueur_exist = coll.find_one({"pseudo": pseudo})
        if joueur_exist is None:
            return "Le joueur avec le pseudo spécifié n'existe pas dans la base de données."
        pseudo_existe_deja = coll.find_one({"pseudo": nouveau_pseudo})
        if pseudo_existe_deja:
            return "Le nouveau pseudo spécifié est déjà utilisé par un autre joueur."
        coll.update_one({"pseudo": pseudo}, {"$set": {"pseudo": nouveau_pseudo}})

        return "Si il existe, ce joueur a été modifié !"

    def display_player(self):
        coll = self.db.personnes
        found = []
        request = coll.find()

        for personne in request:
            filtered_personnes = {
                'prenom': personne.get('prenom', ''),
                'nom': personne.get('nom', ''),
                'date_naissance': personne.get('date_naissance', ''),
                'sexe': personne.get('sexe', ''),
                'pseudo': personne.get('pseudo', ''),
                'victoires': personne.get('victoires', ''),
                'defaites': personne.get('defaites', ''),
                'parties_jouees': personne.get('parties_jouees', '')
            }
            found.append(filtered_personnes)
        return found
