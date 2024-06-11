import services.algorithmes.nombre_participants.utils as utils


def calcul_max_participants(temps_disponible: str, nombre_de_table: int):
    # Calculer la durée d'un match en minutes
    # Calcule duree d'un match
    # Calculer le nombre maximal de matches pouvant être joués avec le temps disponible
    max_matches = utils.calcul_match_max(temps_disponible)
    # Calculer le nombre maximal de participants (chaque match implique deux participants)
    max_participants = max_matches * 2
    return max_participants


def calcul_temps_max(participants: int, nombre_de_table: int):
    nombre_matches = participants // 2 // nombre_de_table
    duree_match = utils.calcule_duree_match()
    temps_total_minutes = nombre_matches * duree_match
    return temps_total_minutes
