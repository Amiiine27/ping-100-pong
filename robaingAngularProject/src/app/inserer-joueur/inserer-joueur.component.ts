import { Component } from '@angular/core';
import {RouterLink, RouterOutlet} from "@angular/router";
import {Player} from "../Player";
import {ApiService} from "../api.service";
import {FormsModule} from "@angular/forms";
import {NgIf} from "@angular/common";
import {response} from "express";
@Component({
  selector: 'app-inserer-joueur',
  standalone: true,
  imports: [RouterOutlet, RouterLink, FormsModule, NgIf],
  templateUrl: './inserer-joueur.component.html',
  styleUrl: './inserer-joueur.component.css'
})
export class InsererJoueurComponent {
  joueurData: Player = {
    nom: '',
    prenom: '',
    date_naissance: '',
    sexe: '',
    pseudo: ''
  };
  messageFromServer : string = '';
  messageFromServer2 : string = '';
  file: File | null = null;

  constructor(private joueurService: ApiService) { }



  onSubmit() {
    this.joueurService.addJoueur(this.joueurData).subscribe(
      (response : string) => {
        this.messageFromServer = response;
      },
    );
  }
  onFileSelected(event: any) {
    this.file = event.target.files[0];
  }
  onFileSubmit(){
    if (this.file){
      this.joueurService.sendFile(this.file).subscribe(
        (response : string) => {
          this.messageFromServer2 = response;
        }
      )
    }
  }
}
