import { Component } from '@angular/core';
import {RouterLink, RouterOutlet} from '@angular/router';
import {ProjetS4Component} from "./projet-s4/projet-s4.component";


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, ProjetS4Component],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'robaingProject';
}
