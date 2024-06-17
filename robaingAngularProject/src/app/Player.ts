export interface Player {
  nom: string;
  prenom: string;
  date_naissance: string;
  sexe: string;
  pseudo: string;
}

export interface DisplayPlayer extends Player {
  victoires: number;
  defaites: number;
  parties_jouees: number;
}

export interface NewNamePlayer {
  old_name: string;
  new_name: string;
}

export interface namePlayer {
  name: string;
}
