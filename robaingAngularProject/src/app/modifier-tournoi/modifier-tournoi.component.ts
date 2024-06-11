import { Component } from '@angular/core';
import {FormsModule} from "@angular/forms";
import {NgIf} from "@angular/common";
import {ApiService} from "../api.service";
import {newDateAndHourTournament} from "../Tournament";

@Component({
  selector: 'app-modifier-tournoi',
  standalone: true,
    imports: [
        FormsModule,
        NgIf
    ],
  templateUrl: './modifier-tournoi.component.html',
  styleUrl: './modifier-tournoi.component.css'
})
export class ModifierTournoiComponent {
  tournoiData: newDateAndHourTournament = {
    nom_tournoi: '',
    date_tournoi: '',
    heure_debut_tournoi : ''
  };

  messageFromServer: string = '';
  constructor(private joueurService: ApiService) {}

  ngOnInit(): void {}
  onSubmit() {
    console.log(this.tournoiData)
    this.joueurService.modDateEtHeureTournoi(this.tournoiData).subscribe(
      (response: string) => {
        this.messageFromServer = response;
      },
    );
  }

}
