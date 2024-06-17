import { Component } from '@angular/core';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {NgIf} from "@angular/common";
import {RouterLink} from "@angular/router";
import {nameTournament} from "../Tournament";
import {ApiService} from "../api.service";

@Component({
  selector: 'app-supprimer-tournoi',
  standalone: true,
    imports: [
        FormsModule,
        NgIf,
        ReactiveFormsModule,
        RouterLink
    ],
  templateUrl: './supprimer-tournoi.component.html',
  styleUrl: './supprimer-tournoi.component.css'
})
export class SupprimerTournoiComponent {
  tournamentData: nameTournament = {
    name:''
  };
  messageFromServer: string = '';

  ngOnInit(): void {}
  constructor(private apiService: ApiService) {}
  onSubmit() {
    this.apiService.delTournament(this.tournamentData).subscribe(
      (response: string) => {
        this.messageFromServer = response;
      },
    );
  }
}
