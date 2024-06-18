from flask import Blueprint, jsonify, request

from AppClasses.Tournoi import (Tournoi, genere_format)

tournoi = Tournoi()

tournois_bp = Blueprint('routes', __name__)


@tournois_bp.route('/', methods=['GET'])
def get_tournois():
    return tournoi.display_tournament(), 200


@tournois_bp.route('/propose_format', methods=['GET'])
def propose_route():
    nombre_participant = int(request.args.get('nombre_participent'))
    nombre_table = int(request.args.get('nombre_table'))
    h, m = [int(x) for x in request.args.get('duree').split(":")]
    duree = h * 60 + m
    choix = genere_format(nombre_participant, nombre_table, duree)
    return jsonify(choix), 200


@tournois_bp.route('/inserer_tournoi', methods=['POST'])
def inserer_tournoi():
    data = request.get_json()
    nom_tournoi = data['nom_tournoi']
    date_tournoi = data['date_tournoi']
    heure_debut_tournoi = data['heure_debut_tournoi']
    nombre_tables = data['nombre_tables']
    joueurs_participants = data['joueurs_participants']
    format = data['format']

    return tournoi.inserer_tournoi(nom_tournoi, date_tournoi, heure_debut_tournoi, nombre_tables,
                                   joueurs_participants, format), 200


@tournois_bp.route('/supprimer_tournoi', methods=['POST'])
def del_tournoi():
    data = request.get_json()
    nom_tournoi = data['name']
    return tournoi.supprimer_tournoi_par_nom(nom_tournoi), 200


@tournois_bp.route('/afficher_match/<nom_tournoi>', methods=['GET'])
def affichage_match(nom_tournoi):
    return jsonify(tournoi.afficher_match(nom_tournoi)), 200


@tournois_bp.route('/modifier_dateheure_tournoi', methods=['PUT'])
def modif_date_heure_tournoi():
    data = request.get_json()
    nom_tournoi = data['nom_tournoi']
    date_tournoi = data['date_tournoi']
    heure_debut_tournoi = data['heure_debut_tournoi']

    return tournoi.modifier_dateheure_tournoi(nom_tournoi, date_tournoi, heure_debut_tournoi), 200


@tournois_bp.route('/mettre_a_jour_tournoi', methods=['PUT'])
def mettre_a_jour_tournoi():
    data = request.get_json()
    nom_tournoi = data['nom_tournoi']
    gagnants = data['liste_gagnants']
    tournoi.mettre_a_jour_tournoi(nom_tournoi, gagnants)
    return "Tournoi mis à jour avec succès", 200


@tournois_bp.route('/get_gagnant/<nom_tournoi>', methods=['GET'])
def get_gagnant(nom_tournoi):
    return jsonify(tournoi.retour_gagnant(nom_tournoi)), 200
