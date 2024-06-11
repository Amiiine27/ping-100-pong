from flask import Blueprint, request, jsonify
from services.algorithmes.tournois import tournois_recherche
from services.algorithmes.tournois import tournois_modification
from services.algorithmes.tournois import tournois_insertion, tournois_gestion_score

tournois_bp = Blueprint('tournois', __name__)


@tournois_bp.route('/', methods=['GET'])
def get_all():
    result = tournois_recherche.tout_les_tournois()
    return jsonify(result)

@tournois_bp.route('/<string:statut>', methods=['GET'])
def get_by_status(statut):
    statut_param = request.view_args['statut']

    if statut_param.lower() == 'true':
        statut_bool = True
    elif statut_param.lower() == 'false':
        statut_bool = False
    else:
        return jsonify({"message": "Statut invalide. Utilisez True ou False."}), 400

    result = tournois_recherche.tournois_statut(statut_bool)
    return jsonify(result)

@tournois_bp.route('/<string:place_name>', methods=['GET'])
def get_by_place_name(place_name):
    result = tournois_recherche.rechercher_tournois_par_lieu(place_name)
    return jsonify(result)


@tournois_bp.route('/', methods=['POST'])
def add_tournoi():
    id = request.json['_id']
    nb_tableau = request.json['nbTableau']
    nom_tournois = request.json['nomTournoi']
    type = request.json['type']
    nature = request.json['nature']
    place_disponible = request.json['placeDisponible']
    statut = request.json['statut']
    date_ouverture = request.json['dateOuverture']
    date_fermeture = request.json['dateFermeture']
    tournois_insertion.insertion_tournoi(id, nb_tableau, nom_tournois, type, nature, place_disponible, statut, date_ouverture, date_fermeture)
    return f"Tu as ajouté un tournoi : {request.json}"


@tournois_bp.route('/tournois_joueur/<string:numero>', methods=['GET'])
def get_tournois_by_numero_joueur(numero):
    result = tournois_recherche.rechercher_tournois_par_numero(numero)
    return jsonify(result)


@tournois_bp.route('/', methods=['PUT'])
def update_tournois():
    modification = request.json
    id_tournois = modification.get('_id')  # Supposons que l'identifiant soit fourni dans le document JSON
    document_modification = modification.get('modification')  # Supposons que les modifications soient fournies dans un champ "modification" dans le JSON
    if not id_tournois:
        return jsonify({"error": "L'identifiant du tournois est manquant"})
    if not document_modification:
        return jsonify({"error": "Les données de modification sont manquantes"})
    tournois_modification.modifier_tournois(id_tournois, document_modification)
    type_modification = document_modification.get('type')
    if type_modification == 'simple':
        tournois_gestion_score.inserer_vainqueur_tournois_simple(id_tournois)
    elif type_modification == 'double':
        tournois_gestion_score.inserer_vainqueur_tournois_double(id_tournois)
    return jsonify({"message": "tournois mis à jour avec succès"})


@tournois_bp.route('/ajouter/<string:id_tournoi>', methods=['PUT'])
def insertion_joueur_tournoi(id_tournoi):
    data = request.json
    numero_inscription = data.get('numeroInscription')
    nom = data.get('nom')
    prenom = data.get('prenom')
    result_messages = tournois_insertion.insertion_joueur_tournoi(id_tournoi, numero_inscription, nom, prenom)
    return jsonify({"messages": result_messages})

@tournois_bp.route('/supprimer/<string:id_tournoi>', methods=['PUT'])
def suppression_joueur_tournoi(id_tournoi):
    data = request.json
    numero_inscription = data.get('numeroInscription')
    result_messages = tournois_insertion.supprimer_joueur_tournoi(id_tournoi, numero_inscription)
    return jsonify({"messages": result_messages})

@tournois_bp.route('/tournois_matchs', methods=['GET'])
def get_tournois_with_matchs():
    matchs = tournois_recherche.tout_les_matchs()
    return jsonify(matchs)
