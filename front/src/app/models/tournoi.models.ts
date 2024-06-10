// Modele pour la table Tournoi


export interface Joueur {
  numeroInscription: string;
  nom: string;
  prenom: string;
 }
 
 
 export interface Adversaire {
  nom: string;
  prenom: string;
 }
 
 
 export interface Match {
  adversaire1: Adversaire[];
  adversaire2: Adversaire[];
 }
 
 
 export interface Tournoi {
  _id: string;
  nomTournoi: string;
  type: string;
  nature: string;
  placeDisponible: number;
  statut: boolean;
  dateOuverture: Date | null;
  dateFermeture: Date | null;
  nbTableau: number;
  joueur:[];
  match: [];
 }
 
 