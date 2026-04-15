def menu():
    print("\n1 - Consulter le catalogue")
    print("2 - Ajouter un Artiste")
    print("3 - Ajouter un Album à un Artiste existant")
    print("4 - Statistiques et rapport")
    print("5 - Quitter l'application")


def sous_menu_1():
    print("\na - Afficher tous les artistes")
    print("b - Rechercher un artiste")
    print("c - Afficher détail artiste")


def sous_menu_2():
    print("\na - Saisir les infos artiste")
    print("b - Vérifier identifiant")
    print("c - Sauvegarder artiste")


def sous_menu_3():
    print("\na - Rechercher artiste par ID")
    print("b - Saisir infos album")
    print("c - Mettre à jour catalogue")


def sous_menu_4():
    print("\na - Top 5 artistes")
    print("b - Moyenne streams par genre")
    print("c - Albums par année")
    print("d - Export rapport CSV")


def main():
    choix = 0
    print("Bienvenue dans mon application")
    while choix != 5:
        menu()
        try:
            choix = int(input("Votre choix : "))
            match choix:
                case 1:
                    sous_menu_1()
                    sous_choix = input("Votre sous-choix : ")
                    match sous_choix:
                     case 'a':
                      #fonction pour la case a
                     case 'b':
                      #fonction pour la case b
                case 2:
                    sous_menu_2()
                    sous_choix = input("Votre sous-choix : ")
                case 3:
                    sous_menu_3()
                    sous_choix = input("Votre sous-choix : ")
                case 4:
                    sous_menu_4()
                    sous_choix = input("Votre sous-choix : ")
                case 5:
                    print("Au revoir !")
                case _:
                    print("Mauvaise valeur")
        except ValueError:
            print("Entrée invalide")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgramme interrompu...")