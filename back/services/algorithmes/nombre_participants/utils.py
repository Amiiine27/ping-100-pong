def convertion_temps(temps_a_convertir: str):
    # Convertir le temps disponible en minutes
    # TODO mettre correctement la conversion
    heures, minutes = map(int, temps_a_convertir.split(','))
    temps_total_minutes = heures * 60 + minutes
    return temps_total_minutes


def calcule_duree_match():
    return 11


def calcul_match_max(temps_disponible: str):
    temp = convertion_temps(temps_disponible)
    duree = calcule_duree_match()
    max_match = temp // duree
    return max_match

