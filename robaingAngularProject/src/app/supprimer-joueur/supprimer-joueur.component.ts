import { Component } from '@angular/core';
import {RouterLink, RouterOutlet} from "@angular/router";
import {FormsModule} from "@angular/forms";
import {NgIf} from "@angular/common";
import {namePlayer} from "../Player";
import {ApiService} from "../api.service";

@Component({
  selector: 'app-supprimer-joueur',
  standalone: true,
  imports: [RouterOutlet, RouterLink, FormsModule, NgIf],
  templateUrl: './supprimer-joueur.component.html',
  styleUrl: './supprimer-joueur.component.css'
})
export class SupprimerJoueurComponent {
  joueurData: namePlayer = {
    name:''
  };
  messageFromServer: string = '';

  ngOnInit(): void {}
  constructor(private joueurService: ApiService) {}
  onSubmit() {
    this.joueurService.delJoueur(this.joueurData).subscribe(
      (response: string) => {
        this.messageFromServer = response;
      },
    );
  }
}
