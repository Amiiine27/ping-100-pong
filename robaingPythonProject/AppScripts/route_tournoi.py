from flask import Blueprint, jsonify, request

from AppClasses.Tournoi import (Tournoi)

tournoi = Tournoi()

tournois_bp = Blueprint('routes', __name__)

@tournois_bp.route('/', methods=['GET'])
def get_tournois():
    return tournoi.display_tournament()

@tournois_bp.route('/inserer_tournoi', methods=['POST'])
def inserer_tournoi():
    data = request.get_json()
    nom_tournoi = data['nom_tournoi']
    date_tournoi = data['date_tournoi']
    heure_debut_tournoi = data['heure_debut_tournoi']
    nombre_tables = data['nombre_tables']
    joueurs_participants = data['joueurs_participants']

    return tournoi.inserer_tournoi(nom_tournoi, date_tournoi, heure_debut_tournoi, nombre_tables, joueurs_participants)

@tournois_bp.route('/supprimer_tournoi', methods=['POST'])
def suppr_tournoi():
    data = request.get_json()
    nom_tournoi = data['name']
    return tournoi.supprimer_tournoi_par_nom(nom_tournoi)

@tournois_bp.route('/afficher_match/<nomTournoi>', methods=['GET'])
def affichage_match(nomTournoi):
    print(jsonify(tournoi.afficher_match(nomTournoi)))
    return jsonify(tournoi.afficher_match(nomTournoi))

@tournois_bp.route('/modifier_dateheure_tournoi', methods=['PUT'])
def modif_dateheure_tournoi():
    data = request.get_json()
    nom_tournoi = data['nom_tournoi']
    date_tournoi = data['date_tournoi']
    heure_debut_tournoi = data['heure_debut_tournoi']

    return tournoi.modifier_dateheure_tournoi(nom_tournoi, date_tournoi, heure_debut_tournoi)

@tournois_bp.route('/mettre_a_jour_tournoi', methods=['PUT'])
def mettre_a_jour_tournoi():
    data = request.get_json()
    nom_tournoi = data['nom_tournoi']
    gagnants = data['liste_gagnants']
    
    print("ici", gagnants)

    tournoi.mettre_a_jour_tournoi(nom_tournoi,gagnants)
    return "Tournoi mis à jour avec succès"

@tournois_bp.route('/get_gagnant/<nomTournoi>', methods=['GET'])
def get_gagnant(nomTournoi):
    return jsonify(tournoi.retour_gagnant(nomTournoi))
