import {HttpClient} from "@angular/common/http";
import {Injectable} from "@angular/core";
import {Observable, catchError, throwError} from "rxjs";
import {Tournoi} from "../models/tournoi.models";
import {Joueur} from "../models/joueur.models";


@Injectable({
 providedIn: 'root'
})
export class TournoiService {
 private protocole = "http";
 private serveur = "localhost:5000";
 private api: string = "/api"


 constructor(private http: HttpClient) {} // Injection du HttpClient pour les requêtes HTTP


 // Récupère la liste des tournois depuis le backend
 getTournois(): Observable<Tournoi[]> {
   const url = `${this.protocole}://${this.serveur}${this.api}/tournois/`;
   return this.http.get<Tournoi[]>(url);
 }


 // Méthode pour récupérer les détails du joueur par numéro de joueur
 getJoueurByNumero(numero: string): Observable<Joueur[]> {
   const url = `${this.protocole}://${this.serveur}${this.api}/joueur/INS/${numero}`;
   return this.http.get<Joueur[]>(url);
 }


 getTournoisOuverts(): Observable<Tournoi[]> {
   const url = `${this.protocole}://${this.serveur}${this.api}/tournois/true`;
   return this.http.get<Tournoi[]>(url).pipe(
     catchError((error) => {
       console.error('Erreur lors de la récupération des tournois ouverts:', error);
       return throwError(error); // Propage l'erreur
     })
   );
 }


 ajouterJoueurTournoi(idTournoi: string, joueurData: { numeroInscription: string, nom: string, prenom: string }): Observable<{ messages: string[] }> {
     console.log('salit')
       console.log(idTournoi)
       const url = `${this.protocole}://${this.serveur}${this.api}/tournois/ajouter/${idTournoi}`;
       console.log(idTournoi)
       return this.http.put<{ messages: string[] }>(url, joueurData);
 }


 supprimerJoueurTournoi(idTournoi: string, numeroInscription: string): Observable<{ messages: string[] }> {
   const url = `${this.protocole}://${this.serveur}${this.api}/tournois/supprimer/${idTournoi}`;
   const data = { numeroInscription };
   return this.http.put<{ messages: string[] }>(url, data);
 }
}

