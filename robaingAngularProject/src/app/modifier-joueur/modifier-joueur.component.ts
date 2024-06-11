import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { NewNamePlayer } from '../Player';
import {FormsModule} from "@angular/forms";
import {NgIf} from "@angular/common";

@Component({
  selector: 'app-modifier-joueur',
  templateUrl: './modifier-joueur.component.html',
  standalone: true,
  imports: [
    FormsModule,
    NgIf
  ],
  styleUrl: './modifier-joueur.component.css'
})
export class ModifierJoueurComponent implements OnInit {
  joueurData: NewNamePlayer = {
    old_name: '',
    new_name: '',
  };

  messageFromServer: string = '';

  constructor(private joueurService: ApiService) {}

  ngOnInit(): void {}

  onSubmit() {
    this.joueurService.modifierJoueurPseudo(this.joueurData).subscribe(
      (response: string) => {
        this.messageFromServer = response;
      },
    );
  }
}
