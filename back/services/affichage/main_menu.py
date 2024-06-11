def afficher_menu():
    while True:
        print("Bienvenue dans l'application de gestion des tournois de tennis de table")
        print("1. Inscrire un joueur")
        print("2. Organiser un tournoi")
        print("3. Afficher les résultats")
        print("4. Quitter")
        try:
            choix = input("Veuillez entrer le numéro de votre choix : ")
            choix = int(choix)
            if choix < 1 or choix > 4:
                raise ValueError
            return str(choix)
        except ValueError:
            print("Choix invalide. Veuillez entrer un numéro valide.")
