import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AccueilComponent } from './accueil/accueil.component';
import { ListeJoueurComponent } from './liste-joueur/liste-joueur.component';
import { InscriptionComponent } from './inscription/inscription.component';
import { PlanDuSiteComponent } from './plan-du-site/plan-du-site.component';
import { ContributeursComponent } from './contributeurs/contributeurs.component';
import { DonneesPersonnellesComponent } from './donnees-personnelles/donnees-personnelles.component';
import { MentionsLegalesComponent } from './mentions-legales/mentions-legales.component';
import { TournoiComponent } from './tournoi/tournoi.component';
import { AjoutTournoiComponent } from './ajout-tournoi/ajout-tournoi.component';
import { ClassementComponent } from './classement/classement.component';


const routes: Routes = [
  { path: '', component: AccueilComponent },
  { path: 'liste-joueur', component: ListeJoueurComponent },
    { path: 'liste-joueur/:nomDuJoueur', component: ListeJoueurComponent },
  { path: 'inscription', component: InscriptionComponent },
  { path: 'plan-du-site', component: PlanDuSiteComponent },
  { path: 'contributeurs', component: ContributeursComponent },
  { path: 'donnees-personnelles', component: DonneesPersonnellesComponent},
  { path: 'mentions-legales', component: MentionsLegalesComponent},
  { path: 'tournoi', component:TournoiComponent},
  { path: 'ajout-tournoi', component:AjoutTournoiComponent},
    { path: 'classement', component: ClassementComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
