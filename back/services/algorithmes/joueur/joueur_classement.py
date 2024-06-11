from services.algorithmes.tournois import tournois_recherche


def calculer_classement_general():
    classement = {}
    tournois = tournois_recherche.tout_les_tournois()

    for tournoi in tournois:
        for match in tournoi['matchs']:
            vainqueur_nom = match['vainqueur']

            if vainqueur_nom != 'match_nul':
                if 'et' in vainqueur_nom:
                    vainqueurs = vainqueur_nom.split(' et ')
                    for vainqueur in vainqueurs:
                        if vainqueur not in classement:
                            classement[vainqueur] = 0
                        classement[vainqueur] += 1
                else:
                    if vainqueur_nom not in classement:
                        classement[vainqueur_nom] = 0
                    classement[vainqueur_nom] += 1

    classement = dict(sorted(classement.items(), key=lambda item: item[1], reverse=True))

    return classement


def afficher_classement(classement):
    classement_json = []
    for i, (nom, victoires) in enumerate(classement.items(), start=1):
        classement_json.append({"Top": i, "Nom": nom, "Victoires": victoires})
    return classement_json
