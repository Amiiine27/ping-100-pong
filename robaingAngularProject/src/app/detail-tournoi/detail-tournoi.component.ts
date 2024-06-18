import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLink, RouterOutlet } from '@angular/router';
import { ApiService } from '../api.service';
import { Matchs, updateTournament } from '../Tournament';
import { NgFor, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-detail-tournoi',
  templateUrl: './detail-tournoi.component.html',
  imports: [RouterOutlet, RouterLink, NgIf, NgFor, FormsModule],
  styleUrl: './detail-tournoi.component.css',
  standalone: true,
})
export class DetailTournoiComponent implements OnInit {
  data: Matchs[] = [];
  nomTournoi: string | null = '';
  gagnants: updateTournament = {
    nom_tournoi: '',
    liste_gagnants: [],
  };
  gagnant: string | null = null;

  constructor(private route: ActivatedRoute, private apiService: ApiService) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      this.nomTournoi = params.get('nomTournoi');
      if (this.nomTournoi != null) {
        this.apiService
          .getWinner(this.nomTournoi)
          .subscribe((response: string) => {
            this.gagnant = response;
          });
        this.apiService
          .getAffichageMatchTournament(this.nomTournoi)
          .subscribe((matchs) => {
            this.data = matchs;
          });
      }
    });
  }

  onSubmit() {
    this.gagnants.liste_gagnants = [];

    this.data.forEach((match, index) => {
      if (match[6] == 'En cours') {
        const radioBtnJ1 = document.getElementById(
          `j1${index}`
        ) as HTMLInputElement;
        const radioBtnJ2 = document.getElementById(
          `j2${index}`
        ) as HTMLInputElement;

        if (radioBtnJ1.checked) {
          const gagnant = {
            joueurs: [match[0], match[1]],
            gagnant: match[0],
            poule: match[5],
          };
          this.gagnants.liste_gagnants.push(gagnant);
        } else if (radioBtnJ2.checked) {
          const gagnant = {
            joueurs: [match[0], match[1]],
            gagnant: match[1],
            poule: match[5],
          };
          this.gagnants.liste_gagnants.push(gagnant);
        }
      }
    });
    this.gagnants.nom_tournoi = this.nomTournoi || '';
    this.apiService.sendWinner(this.gagnants).subscribe(() => {
      window.location.reload();
    });
  }
}
