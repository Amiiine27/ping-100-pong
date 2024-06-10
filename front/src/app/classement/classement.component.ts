import {Component, OnInit} from '@angular/core';
import {JoueurService} from "../services/joueur.service";
import {Classement} from "../models/classement.models";
import {NgForOf} from "@angular/common";
import {RouterLink} from "@angular/router";

@Component({
    selector: 'app-classement',
    templateUrl: './classement.component.html',
    standalone: true,
    imports: [
        NgForOf,
        RouterLink
    ],
    styleUrls: ['./classement.component.css']
})
export class ClassementComponent implements OnInit {
    constructor(private joueurService: JoueurService) {}
    classement: Classement[] = [];

     ngOnInit() {
        this.getClassement();
    }

    getClassement() {
    this.joueurService.getClassement().subscribe((classement: Classement[]) => {
      this.classement = classement;
      console.log(classement);
    });
  }

}
