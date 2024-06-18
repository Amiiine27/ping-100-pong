import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { NgForOf, NgIf } from '@angular/common';
import { Tournament } from '../Tournament';
import { Player } from '../Player';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-inserer-tournoi',
  standalone: true,
  imports: [FormsModule, NgIf, NgForOf],
  templateUrl: './inserer-tournoi.component.html',
  styleUrl: './inserer-tournoi.component.css',
})
export class InsererTournoiComponent {
  tournoiData: Tournament = {
    nom_tournoi: '',
    date_tournoi: '',
    heure_debut_tournoi: '',
    duree_tournoi: '',
    joueurs_participants: [],
    nombre_tables: null as unknown as number,
    liste_matchs: [],
    format: '',
  };
  joueurs: Player[] = [];
  joueurs_selectionnes: Player[] = [];
  messageFromServer: string = '';
  format: any;
  selectedPlayer: Player | null = null;
  protected readonly Math = Math;

  constructor(private tournoiService: ApiService) {}

  ngOnInit(): void {
    this.tournoiService.getAffichageJoueur().subscribe((joueurs: Player[]) => {
      this.joueurs = joueurs;
    });
  }

  addPlayer() {
    if (this.selectedPlayer) {
      this.tournoiData.joueurs_participants.push(this.selectedPlayer.pseudo);
      this.joueurs = this.joueurs.filter(
        (joueur) => joueur !== this.selectedPlayer
      );
      this.joueurs_selectionnes.push(this.selectedPlayer);
      this.selectedPlayer = null;
      if (this.tournoiData.joueurs_participants.length > 3) {
        this.handleShowFormat();
      }
    }
  }

  onSubmit() {
    this.tournoiService
      .addTournoi(this.tournoiData)
      .subscribe((response: string) => {
        this.messageFromServer = response;
      });
  }

  handleShowFormat() {
    let requete = {
      nombre_participent: this.tournoiData.joueurs_participants.length,
      nombre_table: this.tournoiData.nombre_tables,
      duree: this.tournoiData.duree_tournoi,
    };
    this.format = this.tournoiService
      .getChoixFormat(requete)
      .subscribe((response: string) => {
        this.format = response;
        /*
        for (let i = 0; i < this.format.length; i++){
          for (let j = 0; j < this.format [i].length; j++){

        }
      }
        */
        console.log(this.format);
      });
  }

  selectFormat(format: any) {
    this.tournoiData.format = format;
  }

  retirerJoueur(pseudo: string) {
    const index = this.tournoiData.joueurs_participants.indexOf(pseudo);
    if (index != -1) this.tournoiData.joueurs_participants.splice(index, 1);
    this.joueurs_selectionnes.forEach((joueur) => {
      if (joueur.pseudo == pseudo)
        if (this.joueurs.indexOf(joueur) == -1) this.joueurs.push(joueur);
    });
    if (this.tournoiData.joueurs_participants.length > 3) {
      this.handleShowFormat();
    }
  }
}
