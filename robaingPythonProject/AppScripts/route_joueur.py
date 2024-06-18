from flask import Blueprint, jsonify, request

from AppClasses.Joueur import Joueur

joueur = Joueur()
personnes_bp = Blueprint('routes', __name__)


@personnes_bp.route('/', methods=['GET'])
def get_personnes():
    return jsonify(joueur.display_player()), 200


@personnes_bp.route('/inserer_joueur', methods=['POST'])
def inserer_joueur():
    data = request.get_json()
    prenom = data['prenom']
    nom = data['nom']
    date_naissance = data['date_naissance']
    sexe = data['sexe']
    pseudo = data['pseudo']
    return joueur.inserer_joueur(prenom, nom, date_naissance, sexe, pseudo), 200


@personnes_bp.route('/inserer_les_joueurs', methods=['POST'])
def inserer_les_joueurs():
    file = request.files['fichier']
    return joueur.inserer_les_joueurs(file), 200


@personnes_bp.route('/supprimer_joueur', methods=['POST'])
def supprimer_joueur():
    data = request.get_json()
    pseudo = data['name']
    print(pseudo)
    return joueur.supprimer_joueur_par_pseudo(pseudo), 200


@personnes_bp.route('/modifier_joueur', methods=['POST'])
def modifier_joueur():
    data = request.get_json()
    pseudo = data['old_name']
    new_pseudo = data['new_name']
    return joueur.modifier_joueur_par_pseudo(pseudo, new_pseudo), 200
