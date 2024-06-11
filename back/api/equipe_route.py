from flask import Blueprint, request, jsonify
from services.algorithmes.equipe import equipe_recherche
from services.algorithmes.equipe import equipe_modification
from services.algorithmes.equipe import equipe_insertion

equipe_bp = Blueprint('equipe', __name__)


@equipe_bp.route('/', methods=['GET'])
def get_all():
    result = equipe_recherche.toutes_les_equipes()
    return jsonify(result)


@equipe_bp.route('/nom_equipe/<string:team_name>', methods=['GET'])
def get_by_team_name(team_name):
    result = equipe_recherche.recherche_equipe_par_nom(team_name)
    return jsonify(result)


@equipe_bp.route('/nom_equipier/<string:teamplayer_name>', methods=['GET'])
def get_by_teamplayer_name(teamplayer_name):
    result = equipe_recherche.recherche_equipe_par_equipier(teamplayer_name)
    return jsonify(result)


@equipe_bp.route('/', methods=['POST'])
def add_tournoi():
    nom = request.json.get('nom')
    equipe = request.json.get('joueurs')
    equipe_insertion.insertion_equipe(nom, equipe)
    return f"Tu as ajouté une equipe : {request.json}"


@equipe_bp.route('/', methods=['PUT'])
def update_equipe():
    modification = request.json
    id_equipe = modification.get('_id')  # Supposons que l'identifiant soit fourni dans le document JSON
    document_modification = modification.get('modification')  # Supposons que les modifications soient fournies dans un champ "modification" dans le JSON
    if not id_equipe:
        return jsonify({"error": "L'identifiant du equipe est manquant"})
    if not document_modification:
        return jsonify({"error": "Les données de modification sont manquantes"})
    equipe_modification.modifier_equipe(id_equipe, document_modification)
    return jsonify({"message": "equipe mis à jour avec succès"})
