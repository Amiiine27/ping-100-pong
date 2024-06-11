import math
from services.algorithmes.nombre_participants import utils


def calcul_max_participants(temps_disponible: str, nombre_de_parties: int):
    max_match = utils.calcul_match_max(temps_disponible, nombre_de_parties)
    max_participants = 2 ** math.ceil(math.log2(max_match))
    return max_participants

