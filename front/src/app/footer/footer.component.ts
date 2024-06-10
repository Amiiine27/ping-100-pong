import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {
  // Propriétés
  dateDebut = 2024; // Année de début des droits d'auteur
  condition = false; // Condition pour vérifier si la date actuelle est différente de dateDebut
  dateCourante: number; // Année courante

  constructor() {
    // Initialisation de dateCourante dans le constructeur
    this.dateCourante = new Date().getFullYear();
  }

  ngOnInit(): void {
    // Appel de la fonction pour vérifier la condition des droits d'auteur
    this.condition = this.dateCopyRigth(this.dateDebut);
  }

  // Fonction pour vérifier la condition des droits d'auteur
  dateCopyRigth(dateDebut: number): boolean {
    // Vérifie si l'année courante est différente de dateDebut
    return new Date().getFullYear() !== dateDebut;
  }
}
