import { Component } from "@angular/core";
import { Joueur } from "../models/joueur.models";
import { Tournoi } from "../models/tournoi.models";
import { JoueurService } from "../services/joueur.service";
import * as i18nIsoCountries from "i18n-iso-countries";
import localeFr from "i18n-iso-countries/langs/fr.json";
import { TournoiService } from "../services/tournoi.service";

@Component({
    selector: "app-liste-tournoi",
    templateUrl: "./liste-tournoi.component.html",
    styleUrls: ["./liste-tournoi.component.css"],
})
export class ListeTournoiComponent {
    // Déclaration des propriétés utilisées dans le composant
    searchTerm: string = "";
    currentPage: number = 1;
    itemsPerPage: number = 4;
    totalItems: number = 0;
    totalPages: number = 0;
    startItemIndex: number = 1;
    endItemIndex: number = this.itemsPerPage;
    filteredTournois: Tournoi[] = [];
    tournois: Tournoi[] = [];

    // Injection du service JoueurService dans le constructeur
    constructor(private tournoiService: TournoiService) {}

    // Méthode ngOnInit qui s'exécute au moment de l'initialisation du composant
    ngOnInit(): void {
        // Enregistrement de la localisation française pour la librairie i18n-iso-countries
        i18nIsoCountries.registerLocale(localeFr);

        // Récupération des joueurs depuis le service et initialisation de la liste des joueurs avec les codes pays ISO
        this.tournoiService.getTournois().subscribe((data: Tournoi[]) => {
            console.log(data);

            this.tournois = data.map((tournoi) => ({
                ...tournoi,
            }));
            this.filterTournois(); // Filtrage initial des joueurs
        });
    }

    // Méthode pour filtrer les joueurs en fonction du terme de recherche
    filterTournois() {
        this.filteredTournois = this.tournois.filter((tournoi) =>
            tournoi.nomTournoi
                .toLowerCase()
                .includes(this.searchTerm.toLowerCase())
        );
        this.totalItems = this.filteredTournois.length; // Mise à jour du nombre total d'éléments filtrés
        this.calculatePagination(); // Calcul de la pagination en fonction des joueurs filtrés
    }

    // Méthode pour calculer la pagination
    calculatePagination() {
        this.totalPages = Math.ceil(this.totalItems / this.itemsPerPage); // Calcul du nombre total de pages
        this.updatePageItems(); // Mise à jour des indices des éléments de la page courante
    }

    // Méthode pour mettre à jour les indices des éléments de la page courante
    updatePageItems() {
        this.startItemIndex = (this.currentPage - 1) * this.itemsPerPage + 1;
        this.endItemIndex = Math.min(
            this.startItemIndex + this.itemsPerPage - 1,
            this.totalItems
        );
    }

    // Méthode appelée lors du changement de page
    onPageChange(pageNumber: number) {
        this.currentPage = pageNumber;
        this.updatePageItems(); // Mise à jour des éléments de la page après changement
    }

    // Méthode appelée lors du changement du nombre d'éléments par page
    onItemsPerPageChange(newItemsPerPage: number) {
        this.itemsPerPage = newItemsPerPage; // Mise à jour du nombre d'éléments par page
        this.calculatePagination(); // Recalcul de la pagination
        this.currentPage = 1; // Réinitialisation à la première page
        this.updatePageItems(); // Mise à jour des éléments de la page
    }

    // Méthode pour aller à la page précédente
    onPrevPage() {
        if (this.currentPage > 1) {
            this.currentPage--;
            this.updatePageItems(); // Mise à jour des éléments de la page après changement
        }
    }

    // Méthode pour aller à la page suivante
    onNextPage() {
        if (this.currentPage < this.totalPages) {
            this.currentPage++;
            this.updatePageItems(); // Mise à jour des éléments de la page après changement
        }
    }
}
