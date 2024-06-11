import { Routes } from '@angular/router';
import {ProjetS4Component} from "./projet-s4/projet-s4.component";
import {AfficherJoueurComponent} from "./afficher-joueur/afficher-joueur.component";
import {InsererJoueurComponent} from "./inserer-joueur/inserer-joueur.component";
import {ModifierJoueurComponent} from "./modifier-joueur/modifier-joueur.component";
import {SupprimerJoueurComponent} from "./supprimer-joueur/supprimer-joueur.component";
import {InsererTournoiComponent} from "./inserer-tournoi/inserer-tournoi.component"
import {AfficherTournoiComponent} from "./afficher-tournoi/afficher-tournoi.component"
import {SupprimerTournoiComponent} from "./supprimer-tournoi/supprimer-tournoi.component";
import {DetailTournoiComponent} from "./detail-tournoi/detail-tournoi.component";
import {ModifierTournoiComponent} from "./modifier-tournoi/modifier-tournoi.component";



export const routes: Routes = [
  {path: 'projet-s4', component: ProjetS4Component},
  {path: 'afficher-joueur', component: AfficherJoueurComponent},
  {path: 'inserer-joueur', component: InsererJoueurComponent},
  {path: 'modifier-joueur', component: ModifierJoueurComponent},
  {path: 'supprimer-joueur', component: SupprimerJoueurComponent},
  {path: 'inserer-tournoi', component: InsererTournoiComponent},
  {path: 'afficher-tournoi', component: AfficherTournoiComponent},
  {path: 'supprimer-tournoi', component: SupprimerTournoiComponent},
  {path: 'modifier-tournoi', component: ModifierTournoiComponent},
  {path: 'detail-tournoi/:nomTournoi', component: DetailTournoiComponent}
];
