import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Inscription } from '../models/inscription.models';

@Injectable({
  providedIn: 'root'
})
export class InscriptionService {

  private protocole = "http";
  private serveur = "localhost:5000";
  private api: string = "/api"

  constructor(private http: HttpClient) {} // Injection du HttpClient pour les requêtes HTTP

  // Poste les données du formulaire d'inscription
  soumettreInscription(inscriptionData: Inscription) {
    const headers = new HttpHeaders().set('Content-Type', 'application/json');
    const url = `${this.protocole}://${this.serveur}${this.api}/joueur/`;
    return this.http.post<Inscription>(url, inscriptionData,{ headers: headers }); // Ajout de inscriptionData en tant que corps de la requête POST
  }
}
