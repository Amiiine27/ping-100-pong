import { Component } from '@angular/core';
import {ApiService} from "../api.service";
import {AffichageTournament, nameTournament} from "../Tournament";
import {RouterLink} from "@angular/router";
import {NgForOf} from "@angular/common";


@Component({
  selector: 'app-afficher-tournoi',
  standalone: true,
  imports: [
    RouterLink,
    NgForOf
  ],
  templateUrl: './afficher-tournoi.component.html',
  styleUrl: './afficher-tournoi.component.css'
})

export class AfficherTournoiComponent {
  data: AffichageTournament[] = [];

  constructor(private apiService: ApiService) {
  }

  tournamentData: nameTournament = {
    name: ''
  };

  ngOnInit(): void {
    this.apiService.getAffichageTournament().subscribe(response => {
      this.data = response;
      console.log(this.data)
    });
  }

  deleteTournament(nom_tournoi: string) {
    this.tournamentData.name = nom_tournoi
    this.apiService.delTournament(this.tournamentData).subscribe(() => {
      // Supprimez l'élément de la liste des tournois après la suppression
      this.data = this.data.filter(tournament => tournament.nom_tournoi !== nom_tournoi);
    });
  }
}
