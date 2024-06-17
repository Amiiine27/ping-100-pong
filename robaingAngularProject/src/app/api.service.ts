import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Player, NewNamePlayer, namePlayer, DisplayPlayer} from "./Player";
import {
  AffichageTournament,
  nameTournament,
  Tournament,
  Matchs,
  newDateAndHourTournament,
  updateTournament
} from "./Tournament";



@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private http: HttpClient) { }
  getAffichageJoueur(): Observable<DisplayPlayer[]> {
    return this.http.get<DisplayPlayer[]>(`/api/personnes/`)
  }

  getAffichageMatchTournament(nomTournoi: string): Observable<Matchs[]> {
    return this.http.get<Matchs[]>('/api/tournois/afficher_match/' + nomTournoi);
  }

  getWinner(nomTournoi: string): Observable<string> {
    return this.http.get<string>('/api/tournois/get_gagnant/' + nomTournoi);
  }

  getAffichageTournament(): Observable<AffichageTournament[]> {
    return this.http.get<AffichageTournament[]>('/api/tournois')
  }

  addJoueur(player: Player): Observable<string> {
    return this.http.post('/api/personnes/inserer_joueur', player, { responseType: 'text' })
  }

  addTournoi(tournament : Tournament): Observable<string>{
    return this.http.post('/api/tournois/inserer_tournoi', tournament, { responseType: 'text' })
  }

  delJoueur(player: namePlayer): Observable<string> {
    return this.http.post('/api/personnes/supprimer_joueur', player, { responseType: 'text' })
  }

  delTournament(tournament: nameTournament): Observable<string> {
    return this.http.post('/api/tournois/supprimer_tournoi', tournament, { responseType: 'text' })
  }

  sendFile(fichier: File): Observable<string> {
    const formData = new FormData();
    formData.append('fichier', fichier);
    return this.http.post('/api/personnes/inserer_les_joueurs', formData, { responseType: 'text' });
  }

  modifierJoueurPseudo(formData: NewNamePlayer): Observable<string> {
    return this.http.post('/api/personnes/modifier_joueur', formData, { responseType: 'text' });
  }

  modDateEtHeureTournoi(formData: newDateAndHourTournament): Observable<string> {
    return this.http.put('/api/tournois/modifier_dateheure_tournoi', formData, { responseType: 'text' });
  }

    sendWinner(formData: updateTournament):Observable<string> {
      return this.http.put('/api/tournois/mettre_a_jour_tournoi', formData, { responseType: 'text' })
    }
}

