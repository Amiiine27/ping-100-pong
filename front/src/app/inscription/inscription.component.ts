import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Inscription } from '../models/inscription.models';
import { InscriptionService } from '../services/inscription.service';
import { HttpClient } from '@angular/common/http';
import { Pays } from '../models/pays.models';
import { Subject } from 'rxjs';
import { debounceTime, distinctUntilChanged, map } from 'rxjs/operators';

@Component({
  selector: 'app-inscription',
  templateUrl: './inscription.component.html',
  styleUrls: ['./inscription.component.css']
})
export class InscriptionComponent {
  numInscriptionGenererErreur: boolean=false;
  paysListe: Pays[] = [];
  numInscriptionGenerer: string = '';
  filtrePays = new Subject<string>();
  inscriptionModel: Inscription = {
    resultat: '',
    genre: '',
    nom: '',
    prenom: '',
    dateNaissance: null,
    age: null,
    courriel: '',
    telephone: '',
    adresse: '',
    codePostale: null,
    ville: '',
    pays: '',
    numeroInscription: '',
    licence: '',
    classement: null,
    confirmation: false
  };

  constructor(private inscriptionService: InscriptionService, private http: HttpClient) {
    this.chargerPays();
    this.initialiserFiltrePays();
  }

  onSubmit(inscriptionForm: NgForm) {
  console.log('Tentative de soumission du formulaire...');
  if (inscriptionForm.valid) {
    console.log('Formulaire valide, envoi des données au serveur...');
    if (this.inscriptionModel.dateNaissance) {
      this.inscriptionModel.age = this.calculerAge(new Date(this.inscriptionModel.dateNaissance));
    }
    this.inscriptionService.soumettreInscription(this.inscriptionModel).subscribe(
      response => {
        console.log('Réponse de l\'API:', response);
        if (response.numeroInscription) {
          this.numInscriptionGenererErreur = false;
          inscriptionForm.reset();
          this.numInscriptionGenerer = response.numeroInscription;
        } else {
          this.numInscriptionGenererErreur = true;
        }
      },
      error => {
        console.error('Erreur lors de l\'inscription', error);
      }
    );
  } else {
    console.log('Formulaire invalide, soumission annulée.');
  }
}

  initialiserFiltrePays() {
    this.filtrePays.pipe(
      debounceTime(200),
      distinctUntilChanged(),
      map(terme => terme ? this.recherchePays(terme) : this.paysListe.slice())
    ).subscribe(paysFiltres => {
      this.paysListe = paysFiltres;
    });
  }

  recherchePays(terme: string): Pays[] {
    return this.paysListe.filter(pays => pays.nom.toLowerCase().indexOf(terme.toLowerCase()) > -1);
  }

  chargerPays() {
    this.http.get<{countries: {[key: string]: string}}>('assets/data/pays.json').subscribe(data => {
      this.paysListe = Object.entries(data.countries).map(([code, nom]) => ({code, nom}));
    });
  }

  private calculerAge(dateNaissance: Date): number {
    const aujourdHui = new Date();
    const anneeActuelle = aujourdHui.getFullYear();
    const moisActuel = aujourdHui.getMonth();
    const jourActuel = aujourdHui.getDate();

    const anneeNaissance = dateNaissance.getFullYear();
    const moisNaissance = dateNaissance.getMonth();
    const jourNaissance = dateNaissance.getDate();

    let age = anneeActuelle - anneeNaissance;

    if (moisActuel < moisNaissance || (moisActuel === moisNaissance && jourActuel < jourNaissance)) {
      age--;
    }

    return age;
  }
}
