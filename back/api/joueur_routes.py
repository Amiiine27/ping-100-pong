from flask import Blueprint, request, jsonify
from services.algorithmes.joueur import joueur_recherche
from services.algorithmes.joueur import joueur_modification
from services.algorithmes.joueur import joueur_insertion, joueur_classement
from services.algorithmes.joueur.joueur_verif import joueur_existe

joueur_bp = Blueprint('joueur', __name__)


@joueur_bp.route('/', methods=['GET'])
def get_all():
    result = joueur_recherche.tout_les_joueurs()
    return jsonify(result)


@joueur_bp.route('/<string:joueurs_name>', methods=['GET'])
def get_by_name(joueurs_name):
    result = joueur_recherche.recherche_joueur(joueurs_name)
    return jsonify(result)


@joueur_bp.route('/INS/<string:joueur_numero>', methods=['GET'])
def get_by_numero(joueur_numero):
    result = joueur_recherche.recherche_par_numero(joueur_numero)
    return jsonify(result)


@joueur_bp.route('/', methods=['POST'])
def add_joueur():
    print(request.json)
    nom = request.json.get('nom')
    prenom = request.json.get('prenom')
    genre = request.json.get('genre')
    age = request.json.get('age')
    courriel = request.json.get('courriel')
    telephone = request.json.get('telephone')
    adresse = request.json.get('adresse')
    codePostale = request.json.get('codePostale')
    ville = request.json.get('ville')
    pays = request.json.get('pays')
    licence = request.json.get('licence')
    classement = request.json.get('classement')

    if joueur_existe(nom, prenom, age=age, genre=genre):
        return jsonify("Le joueur existe deja !")

    result = joueur_insertion.insertion_joueur(genre, nom, prenom, age, courriel, telephone, adresse, codePostale, ville, pays, licence, classement)
    print(result)
    return jsonify(result)


@joueur_bp.route('/', methods=['PUT'])
def update_joueur():
    modification = request.json
    id_joueur = modification.get('_id')
    document_modification = modification.get('modification')
    if not id_joueur:
        return jsonify({"error": "L'identifiant du joueur est manquant"})
    if not document_modification:
        return jsonify({"error": "Les données de modification sont manquantes"})
    joueur_modification.modifier_joueur(id_joueur, document_modification)
    return jsonify({"message": "Joueur mis à jour avec succès"})


@joueur_bp.route('/classement', methods=['GET'])
def afficher_classement():
    classement = joueur_classement.calculer_classement_general()
    return joueur_classement.afficher_classement(classement)
