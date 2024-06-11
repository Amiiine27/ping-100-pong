import { LOCALE_ID, NgModule } from '@angular/core';
import { registerLocaleData } from '@angular/common';
import localeFr from '@angular/common/locales/fr';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AccueilComponent } from './accueil/accueil.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { ListeJoueurComponent } from './liste-joueur/liste-joueur.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { InscriptionComponent } from './inscription/inscription.component';
import { PlanDuSiteComponent } from './plan-du-site/plan-du-site.component';
import { ContributeursComponent } from './contributeurs/contributeurs.component';
import { MentionsLegalesComponent } from './mentions-legales/mentions-legales.component';
import { DonneesPersonnellesComponent } from './donnees-personnelles/donnees-personnelles.component';
import { NgSelectModule } from '@ng-select/ng-select';
import { TournoiComponent } from './tournoi/tournoi.component';
import { AjoutTournoiComponent } from './ajout-tournoi/ajout-tournoi.component';
import { ClassementComponent } from './classement/classement.component';
import { ListeTournoiComponent } from './liste-tournoi/liste-tournoi.component';

registerLocaleData(localeFr);

@NgModule({
  declarations: [
    AppComponent,
    AccueilComponent,
    HeaderComponent,
    FooterComponent,
    ListeJoueurComponent,
    InscriptionComponent,
    PlanDuSiteComponent,
    ContributeursComponent,
    MentionsLegalesComponent,
    DonneesPersonnellesComponent,
    TournoiComponent,
    AjoutTournoiComponent,
    ListeTournoiComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    NgSelectModule
  ],
  providers: [
    { provide: LOCALE_ID, useValue: 'fr-FR' } // Utiliser la locale française
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
