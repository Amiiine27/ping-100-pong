export interface Inscription {
  resultat: string,
  // identité du joueur
  genre: string; //femme ou homme
  nom: string; //dupont
  prenom: string;//paul
  dateNaissance : Date | null; // 23/02/2004
  courriel: string, //toto@gmail.fr
  telephone: string, //01 01 01 01 01
  age : number | null; //calculer l'age en fonction de la date de Naissance
  adresse : string; // 106 rue de la porte
  codePostale : number | null; //93323
  ville: string; //Paris
  pays: string; //France
  //Info joueurs
  numeroInscription: string, //12ABC23350F(a generer clé unique)
  licence: string; //amateur ou pro
  classement : number | null; //rien ou 15
  confirmation: boolean; //oui ou non
}
/**Pour le formulaire des joueurs j'utilise:
 * Nom
 * prenom
 * date de naissance
 * pays
 * licence
 * genre
 */

/**Pour le formulaire d'inscription j'utilise:
  genre
  nom
  prenom
  dateNaissance
  adresseMail
  telephone
  adresse
  codePostale
  ville
  pays
  numeroInscription
  licence: string
  classement
 */

  /**Pour le formulaire d'inscription a un tournoi :
   * numeroInscription
   * nom
   * prenom
   * nom du tournoi (ex. T1, T2,...)
   * type (valeur possible : simple ou double)
   * nature (valeur possible : mixte, femme, homme)
   * placeDisponibleSimple (5 pour un nouveau tournoi)
   * placeDisponibleDouble (5 pour un nouveau tournoi)
   * statut: (true=ouvert, false=fermé) --> pour ouvrir un nouveau tounoi
   * DateOuverture: date --> au moment ou le tournoi est plein
   * Datefermeture:  date --> fin du tounoi = dateDebut +2 jours
   */

  /** Pour afficher les resultats :
   * numeroInscription
   * nom
   * prenom
   * nomAdversaire
   * prenomAdversaire
   * nom du tournoi (ex. T1, T2,...)
   * type (valeur possible : simple ou double)
   * nature (valeur possible : mixte, femme, homme)
   * statut: (true=ouvert, false=fermé) --> pour ouvrir un nouveau tounoi
   * DateOuverture: date --> au moment ou le tournoi est plein
   * Datefermeture:  date --> fin du tounoi = dateDebut +2 jours
   * resultatFinal: gagnant/perdant
   * scoreDuMatch: 21 - 2
   * totalPoint: (0 perdu, 5 null, 10 gagné)
   */
