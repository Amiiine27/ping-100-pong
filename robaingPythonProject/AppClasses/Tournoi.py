import math
from datetime import datetime, timedelta

from bson import max_key

from AppClasses.Connexion import Connexion
from AppScripts.methodesUtiles import *


def est_puissance_de_2(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0


def calcul_duree_poule(taille_poule, nb_table):
    return math.ceil(taille_poule * (taille_poule - 1) / 2 / nb_table * 5)


def determine_poule(nb_participants, nb_poule):
    return [nb_participants // nb_poule + (j and nb_participants % 2) for j in range(2)] if nb_poule == 2 else [
        nb_participants // nb_poule + j for j in [nb_participants / nb_poule % 1 >= 0.25 * k for k in range(1, 5)]]


def genere_format(nb_participants, nb_table, temps_max):
    choix = []
    duree_championat = calcul_duree_poule(nb_participants, nb_table)
    if nb_participants <= 8 and duree_championat <= temps_max:
        choix += [("RONDE", duree_championat)]

    duree_championat = sum(
        nb_participants / (2 ** x) for x in range(1, int(math.log2(nb_participants) + 1))) * 5 / nb_table
    if est_puissance_de_2(nb_participants) and duree_championat <= temps_max:
        choix += [("BRAQUET", duree_championat)]

    nb_joueurs_brackets = 4
    if nb_participants < nb_joueurs_brackets:
        return choix

    for nb_poule in [2, 4]:
        poules = determine_poule(nb_participants, nb_poule)
        if 2 in poules or 1 in poules:
            continue
        temp_tournoi = 5 * (3 if nb_table == 1 else 2) + sum(calcul_duree_poule(p, nb_table) for p in poules)
        if temp_tournoi <= temps_max:
            choix += [(f"POULE :{poules}", temp_tournoi)]
    return choix


def joue_deja_a_cette_heure(joueur_1: str, heure_match: datetime, liste_matchs: list):
    if not liste_matchs:
        return False
    for match in liste_matchs:
        if (joueur_1 == match[0] or joueur_1 == match[1]) and match[3] == heure_match.strftime(
                "%H:%M le %d.%m.%Y"):
            return True
    return False


def horaire_complet(nb_table: int, liste_matchs: list, heure_match: datetime):
    if not liste_matchs:
        return False
    compteur = 0
    for match in liste_matchs:
        if match[3] == heure_match.strftime("%H:%M le %d.%m.%Y"):
            compteur += 1
    return compteur == nb_table


def calcul_nb_phase(nb_joueurs):
    while nb_joueurs > 0:
        return


def nb_match_a_cette_heure(liste_match: list, heure_match: datetime):
    """
    Ici, on calcule le nombre de matchs à
    un horaire donné, mais la fonction a
    pour finalité d'attribuer un numéro
    de table à chaque match
    """

    if not liste_match:
        return 1
    compteur = 1
    for match in liste_match:
        if heure_match.strftime("%H:%M le %d.%m.%Y") == match[3]:
            compteur += 1
    return compteur


class Tournoi(Connexion):

    def __init__(self):
        Connexion.__init__(self)

    def inserer_tournoi(self, nom_tournoi: str,
                        date_debut_tournoi: str,
                        heure_debut_tournoi: str,
                        nombre_de_table: int,
                        liste_des_joueurs: list,
                        format: list):

        if not (nom_tournoi and date_debut_tournoi and heure_debut_tournoi and nombre_de_table and liste_des_joueurs):
            return "Certains paramètres sont vides ou nuls"

        if not liste_des_joueurs:
            return "La liste des joueurs est vide"

        liste_de_matchs = self.generer_tournoi_2(liste_des_joueurs, nombre_de_table,
                                                 datetime.strptime(date_debut_tournoi + " " + heure_debut_tournoi,
                                                                   "%Y-%m-%d %H:%M"), format)
        coll = self.db.tournoi
        if self.tournoi_existe(nom_tournoi):
            return "Un tournoi ayant ce nom existe déjà"
        else:
            coll.insert_one(
                {"nom_tournoi": nom_tournoi, "date_debut_tournoi": date_debut_tournoi,
                 "heure_debut_tournoi": heure_debut_tournoi, "nombres_de_tables": nombre_de_table,
                 "liste_des_joueurs": liste_des_joueurs, "liste_des_matchs": liste_de_matchs,
                 "format": format[0]}
            )
            return "Tournoi inséré"

    def tournoi_existe(self, nom_tournoi: str):
        coll = self.db.tournoi
        requete = coll.find_one({"nom_tournoi": nom_tournoi})
        if requete is not None:
            return True
        else:
            return False

    def modifier_dateheure_tournoi(self, nom_tournoi: str, date_debut_tournoi: str, heure_debut_tournoi: str):
        coll = self.db.tournoi

        if self.tournoi_existe(nom_tournoi):
            tournoi_existant = coll.find_one({"nom_tournoi": nom_tournoi})
            liste_des_joueurs = tournoi_existant.get("liste_des_joueurs")
            nombre_de_table = tournoi_existant.get("nombres_de_tables")

            liste_de_matchs = self.generer_tournoi(liste_des_joueurs, nombre_de_table,
                                                   datetime.strptime(date_debut_tournoi + " " + heure_debut_tournoi,
                                                                     "%Y-%m-%d %H:%M"))

            coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {
                "date_debut_tournoi": date_debut_tournoi,
                "heure_debut_tournoi": heure_debut_tournoi,
                "liste_des_matchs": liste_de_matchs
            }})

            return "La date et l'heure du tournoi ont été mis à jour"
        else:
            return "Le tournoi n'existe pas"

    def afficher_match(self, nom_tournoi: str):
        coll = self.db.tournoi
        tournoi = coll.find_one({"nom_tournoi": nom_tournoi})
        if tournoi:
            matches = tournoi.get('liste_des_matchs', [])
            return matches
        else:
            return []

    def definir_format_tournoi(self, nb_joueur: int) -> str:
        if est_puissance_de_2(nb_joueur) and nb_joueur <= 32:
            return "Elimination Simple"  # Des tournois à élimination simple: pour 32 joueurs par exemple on aura 16
            # matchs, 16 survivants puis 8 matchs 8 survivants, etc...
        elif nb_joueur < 10:
            return "Tournoi à la ronde"  # Un format de tournoi rapide ou tout le monde rencontre tout le monde et la
            # personne avec le plus de victoires gagne.
        elif nb_joueur < 32:
            return "rienpourlemoment"  # Comme le tournoi à élimination simple mais certains joueurs auront
            # la chance de passer directement en deuxième phase.
        else:
            return "rienpourlemoment"  # Des poules de 3 à 4 joueurs qui élimineront 1 joueur si
            # 3 joueurs dans la poule et 2 joueurs si 4 joueurs dans la poule.

    def generer_tournoi_2(self, joueurs: list, nb_table: int, date_heure_debut: datetime, format: list):
        if "RONDE" in format[0]:
            pass
        else:  # avec poules
            _, poules = format[0].split(':')
            poules = [int(x) for x in poules.replace('[', '').replace(']', '').split(',')]
            matchs_poules = [
                [(joueurs[x + sum(poules[:i])], joueurs[y + + sum(poules[:i])]) for x in range(k) for y in range(x)] for
                i, k in enumerate(poules)]
            matchs_ordoner = []
            nb_match_poules = sum(x * (x - 1) / 2 for x in poules)
            index_poule = 0
            compteur_table = 0
            while len(matchs_ordoner) < nb_match_poules:
                if matchs_poules[index_poule]:
                    t = matchs_poules[index_poule].pop(0)
                    matchs_ordoner.append([
                        t[0],
                        t[1],
                        "Table " + str(compteur_table + 1),
                        date_heure_debut.strftime("%H:%M le %d.%m.%Y"),
                        date_heure_debut,
                        "Poule " + str(index_poule),
                        "En cours"
                    ])
                    compteur_table = (compteur_table + 1) % nb_table
                    if not compteur_table:
                        date_heure_debut += timedelta(minutes=5)
                index_poule = (index_poule + 1) % len(poules)
            return matchs_ordoner

    def mettre_a_jour_tournoi(self, nom_tournoi: str, gagnants: list):
        coll = self.db.tournoi
        tournoi = coll.find_one({"nom_tournoi": nom_tournoi})
        if "POULE" in tournoi.get('format'):
            self.gere_poule(nom_tournoi, gagnants)
        elif "Demi-final" in tournoi.get('format'):
            self.gere_demi_final(nom_tournoi, gagnants)

    def gere_poule(self, nom_tournoi, gagnants):
        coll = self.db.tournoi
        tournoi = coll.find_one({"nom_tournoi": nom_tournoi})
        nombre_table = tournoi.get('nombres_de_tables')
        _, format = tournoi.get('format').split(':')
        format = [int(x) for x in format.replace('[', '').replace(']', '').split(',')]

        matchs = tournoi.get("liste_des_matchs")

        for gagnant in gagnants:
            for m in matchs:
                if m[0] == gagnant["joueurs"][0] and m[1] == gagnant["joueurs"][1]:
                    m[6] = gagnant["gagnant"]

        for m in matchs:
            if m[6] == 'En cours':
                coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {"liste_des_matchs": matchs}})
                return

        coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {"liste_des_matchs": matchs}})
        poules = [{} for _ in range(len(format))]

        for m in matchs:
            if "Poule" in m[5]:
                if m[0] not in poules[int(m[5][-1])]:
                    poules[int(m[5][-1])][m[0]] = 0
                if m[1] not in poules[int(m[5][-1])]:
                    poules[int(m[5][-1])][m[1]] = 0
                poules[int(m[5][-1])][m[6]] += 1

        finalistes = []

        for p in poules:
            sorted_items = sorted(p.items(), key=lambda item: item[1], reverse=True)
            if len(format) == 4:
                print(sorted_items[0])
                finalistes.append(sorted_items[0])
            elif len(format) == 2:
                top_two = sorted_items[:2]
                for t in top_two:
                    finalistes += [t]

        new_match = [
            [
                finalistes[0][0],
                finalistes[1][0],
                "Table 1",
                "todo time",
                "todo time",
                "Demi-final",
                "En cours"
            ],
            [
                finalistes[2][0],
                finalistes[3][0],
                "Table 1" if nombre_table == 1 else "Table 2",
                "todo time",
                "todo time",
                "Demi-final",
                "En cours"
            ]
        ]
        coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {"format": "Demi-final"}})
        coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {"liste_des_matchs": new_match}})

    def gere_demi_final(self, nom_tournoi, gagnants):
        coll = self.db.tournoi
        tournoi = coll.find_one({"nom_tournoi": nom_tournoi})
        matchs = tournoi.get("liste_des_matchs")

        for gagnant in gagnants:
            for m in matchs:
                if m[0] == gagnant["joueurs"][0] and m[1] == gagnant["joueurs"][1]:
                    m[6] = gagnant["gagnant"]

        for m in matchs:
            if m[6] == 'En cours':
                coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {"liste_des_matchs": matchs}})
                return

        coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {"liste_des_matchs": matchs}})

        finalistes = []

        for m in matchs:
            finalistes += [m[6]]

        new_match = [
            [
                finalistes[0],
                finalistes[1],
                "Table 1",
                "todo time",
                "todo time",
                "Finale",
                "En cours"
            ]
        ]

        coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {"format": "Finale"}})
        coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {"liste_des_matchs": new_match}})

    def display_tournament(self):
        coll = self.db.tournoi
        found = []
        request = coll.find()

        for tournoi in request:
            filtered_tournament = {
                'nom_tournoi': tournoi.get('nom_tournoi', ''),
                'date_tournoi': tournoi.get('date_debut_tournoi', ''),
                'heure_debut_tournoi': tournoi.get('heure_debut_tournoi', ''),
                'nombre_participants': len(tournoi.get('liste_des_joueurs', []))
            }
            found.append(filtered_tournament)

        return found

    def supprimer_tournoi_par_nom(self, tournoi: str):
        coll = self.db.tournoi
        joueur = coll.find_one({"nom_tournoi": tournoi})
        if joueur:
            coll.delete_one({"nom_tournoi": tournoi})
            return "Ce tournoi a été supprimé ! :)"
        else:
            return "Le tournoi avec le nom donné n'existe pas dans la base de données."

    def retour_gagnant(self, nom_tournoi: str):
        coll = self.db.tournoi
        tournoi = coll.find_one({"nom_tournoi": nom_tournoi})
        joueurs = self.db.joueurs

        if tournoi:
            gagnant = tournoi.get("gagnant")
            if gagnant is not None:
                joueurs.update_one({"pseudo": gagnant}, {"$inc": {"victoires": 1}})

                for joueur in tournoi.get("liste_des_joueurs", []):
                    if joueur != gagnant:
                        joueurs.update_one({"pseudo": joueur}, {"$inc": {"defaites": 1}})
                return gagnant
        return "null"
