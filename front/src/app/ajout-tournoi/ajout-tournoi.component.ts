import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AjoutTournoiService } from '../services/ajout-tournoi.service';
import { HttpClient } from '@angular/common/http';
import { Tournoi } from '../models/tournoi.models';


@Component({
 selector: 'app-ajout-tournoi',
 templateUrl: './ajout-tournoi.component.html',
 styleUrls: ['./ajout-tournoi.component.css']
})
export class AjoutTournoiComponent {
 tournoiModel : Tournoi= {
   _id: '',
   nomTournoi: '',
   type: '',
   nature: '',
   placeDisponible: 0 ,
   statut: true,
   dateOuverture: null,
   dateFermeture: null,
   nbTableau: 0,
   joueur: [],
   match: [],
 };
 messageSuccess: string = '';
 messageError: string = '';


 constructor(private ajoutTournoiService:  AjoutTournoiService, private http: HttpClient) {
 }


 onSubmit(tournoiForm: NgForm) {
   if (tournoiForm.valid) {
     this.ajoutTournoiService.soumettreTournois(this.tournoiModel).subscribe(
       response => {
         if (!response) {
           tournoiForm.reset();
           this.messageSuccess = 'Tournoi ajouté avec succès !';
            alert(JSON.stringify(response));
           this.messageError = '';
         }
       },
     );
   } else {
     console.log('Formulaire invalide, soumission annulée.');
     this.messageError = 'Le formulaire est invalide. Veuillez vérifier vos données.';
     this.messageSuccess = '';
   }
 }
}


