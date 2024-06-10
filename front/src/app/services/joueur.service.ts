import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Joueur } from '../models/joueur.models';
import {Classement} from "../models/classement.models";

@Injectable({
  providedIn: 'root' // Ce service est disponible globalement dans l'app
})
export class JoueurService {
  private protocole = "http";
  private serveur = "localhost:5000";

  constructor(private http: HttpClient) {} // Injection du HttpClient pour les requêtes HTTP

  // Récupère la liste des joueurs depuis le backend
  getJoueurs() {
    const url = `${this.protocole}://${this.serveur}/api/joueur/`;
    return this.http.get<Joueur[]>(url); // Retourne un Observable de Joueur[]
  }
  getClassement(){
   const url = `${this.protocole}://${this.serveur}/api/joueur/classement`;
   return this.http.get<Classement[]>(url);
}

}
