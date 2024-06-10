from services.algorithmes.tournois import tournois_modification
from services.algorithmes.tournois import tournois_recherche
from services.algorithmes.tournois import tournois_gestion_score
def afficher_matchs_tournoi(tournoi):
    matchs = tournoi.get('matchs', [])
    if not matchs:
        print("Aucun match trouvé pour ce tournoi.")
        return

    print("Voici les matchs du tournoi :")
    for match in matchs:
        joueurs = match.get('joueurs', [])

        if joueurs:
            joueur1 = joueurs[0]['nom'] + ' ' + joueurs[0]['prenom']
            joueur2 = joueurs[1]['nom'] + ' ' + joueurs[1]['prenom']
            print(f"Match : {joueur1} contre {joueur2}")
            print()

def creer_matchs_simple(joueurs):
    matchs = []

    for i in range(len(joueurs)):
        for j in range(i + 1, len(joueurs)):
            joueur1 = {"nom": joueurs[i]['nom'], "prenom": joueurs[i]['prenom']}
            joueur2 = {"nom": joueurs[j]['nom'], "prenom": joueurs[j]['prenom']}
            match = {
                "match": {
                    "adversaire1": joueur1,
                    "adversaire2": joueur2,
                }
            }
            matchs.append(match)
    return matchs


def creer_matchs_double(joueurs):
    matchs = []
    # Regrouper les joueurs par paires
    paires = []
    for i in range(0, len(joueurs), 2):
        if i + 1 < len(joueurs):
            paire = [joueurs[i], joueurs[i + 1]]
            paires.append(paire)

    for i in range(len(paires)):
        for j in range(i + 1, len(paires)):
            adversaire1 = paires[i]
            adversaire2 = paires[j]
            match = {
                "match": {
                    "adversaire1": [
                        {"nom": adversaire1[0]['nom'], "prenom": adversaire1[0]['prenom']},
                        {"nom": adversaire1[1]['nom'], "prenom": adversaire1[1]['prenom']}
                    ],
                    "adversaire2": [
                        {"nom": adversaire2[0]['nom'], "prenom": adversaire2[0]['prenom']},
                        {"nom": adversaire2[1]['nom'], "prenom": adversaire2[1]['prenom']}
                    ]
                }
            }
            matchs.append(match)

    return matchs


def gestion_matchs(id):

    tournois = tournois_recherche.trouver_tournoi_par_id(id)
    matchs = []
    if tournois:
        if not tournois['statut']:
            joueurs = tournois.get("joueurs", [])
            if tournois['type'] == "simple":
                matchs = creer_matchs_simple(joueurs)
            elif tournois['type'] == "double":
                matchs = creer_matchs_double(joueurs)
            if matchs:
                tournois_modification.modifier_match_tournois(id, matchs)
                tournois_gestion_score.initialiser_scores(id, matchs)

            else:
                print("Aucun match n'a été créé.")
    else:
        print("Tournoi non trouvé.")
