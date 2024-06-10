import { Component, OnInit } from '@angular/core';
import { Tournoi } from '../models/tournoi.models';
import { TournoiService } from '../services/tournoi.service';
import { Router } from '@angular/router';


@Component({
 selector: 'app-tournoi',
 templateUrl: './tournoi.component.html',
 styleUrls: ['./tournoi.component.css']
})
export class TournoiComponent implements OnInit {
 numeroInscription: string = '';
 inscriptionValide: boolean | null = null;
 messageValidation: string = '';
 fieldsetOpen: boolean = true;
 tournois: Tournoi[] = [];
 nomJoueur: string = '';
 prenomJoueur: string = '';
 idTournoi: string = '';
 constructor(private tournoiService: TournoiService, private router: Router) {
 }


 ngOnInit(): void {
 }


 getTournoisOuverts(): void {
   this.tournoiService.getTournoisOuverts().subscribe((tournois: Tournoi[]) => {
     this.tournois = tournois;
     console.log(tournois)
   });
 }
 onChange(event: Event, idTournoi: string): void {
   if (event.target !== null && 'checked' in event.target) {
       const isChecked: boolean = (event.target as HTMLInputElement).checked;
       if (isChecked && this.inscriptionValide) {
           //idTournoi = this.idTournoi
           console.log('je suis la ')
           console.log(this.tournois[0])
           this.tournoiService.ajouterJoueurTournoi(idTournoi, {
               numeroInscription: this.numeroInscription,
               nom: this.nomJoueur,
               prenom: this.prenomJoueur
           }).subscribe({
               next: (response) => {
                   console.log('Joueur ajouté avec succès', response);
                   alert(JSON.stringify(response));
               },
               error: (error) => {
                   console.error('Erreur lors de l\'ajout du joueur', error);
               }
           });
       } else {
            console.log(this.numeroInscription)
           this.tournoiService.supprimerJoueurTournoi(idTournoi, this.numeroInscription)
               .subscribe({
                   next: (response) => {
                       console.log('Joueur supprimé avec succès', response);
                       alert(JSON.stringify(response));
                       // Traiter la réponse ou effectuer d'autres actions ici
                   },
                   error: (error) => {
                       console.error('Erreur lors de la suppression du joueur', error);
                   }
               });
       }
   }
 }


 voirNouveauxTournois(): void {
   this.getTournoisOuverts();
 }


 voirTournoisInscrits(): void {
   // Implémentez ici la logique pour afficher les tournois inscrits
 }


 validerNumeroInscription(): void {
   this.tournoiService.getJoueurByNumero(this.numeroInscription).subscribe(
       (data: any[]) => {
         if (data.length !== 0) {
           this.inscriptionValide = true;
           this.messageValidation = 'Bonjour ' + data[0].prenom + ' ' + data[0].nom + '.';
           this.nomJoueur = data[0].nom
             this.prenomJoueur = data[0].prenom
         } else {
           this.inscriptionValide = false;
           this.messageValidation = 'Numéro d’inscription non valide. Veuillez réessayer.';
         }
       },
       (error: any) => {
         console.error('Erreur lors de la validation du numéro d\'inscription', error);
       }
   );
 }






 ouvrirPageAjoutTournois() {
   this.router.navigate(['/ajout-tournoi']);
 }
}

