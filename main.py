import label
import analyse

CHEMIN = "catalogue.json"


def menu():
    print("\n=== SahelSound Records ===")
    print("1 - Consulter le catalogue")
    print("2 - Ajouter un artiste")
    print("3 - Ajouter un album à un artiste existant")
    print("4 - Statistiques et rapport")
    print("5 - Quitter l'application")


def sous_menu_1():
    print("\na - Afficher tous les artistes")
    print("b - Rechercher un artiste par nom ou genre")
    print("c - Afficher le détail d'un artiste")


def sous_menu_4():
    print("\na - Top 5 des artistes par nombre total de streams")
    print("b - Moyenne des streams par genre musical")
    print("c - Nombre d'albums sortis par année")
    print("d - Exporter le rapport complet dans rapport.csv")


def main():
    catalogue = label.charger_catalogue(CHEMIN)
    print("Bienvenue dans SahelSound Records !")
    choix = 0
    while choix != 5:
        menu()
        try:
            choix = int(input("Votre choix : "))
            match choix:
                case 1:
                    sous_menu_1()
                    sous_choix = input("Votre sous-choix : ").strip().lower()
                    match sous_choix:
                        case 'a':
                            label.lister_artistes(catalogue)
                        case 'b':
                            critere = input("Rechercher par (nom/genre) : ").strip().lower()
                            if critere not in ('nom', 'genre'):
                                print("Critère invalide. Utilisez 'nom' ou 'genre'.")
                            else:
                                valeur = input(f"Valeur ({critere}) : ").strip()
                                resultats = label.rechercher_artiste(catalogue, critere, valeur)
                                if resultats:
                                    label.lister_artistes(resultats)
                                else:
                                    print("Aucun artiste trouvé.")
                        case 'c':
                            id_artiste = input("ID de l'artiste : ").strip()
                            label.afficher_detail_artiste(catalogue, id_artiste)
                        case _:
                            print("Sous-choix invalide.")
                case 2:
                    print("\n=== Ajout d'un artiste ===")
                    artiste = label.saisir_infos_artiste()
                    if not label.verifier_identifiant(catalogue, artiste["id"]):
                        print("Cet identifiant existe déjà. Artiste non ajouté.")
                    else:
                        catalogue = label.ajouter_artiste(catalogue, artiste)
                        label.sauvegarder_catalogue(catalogue, CHEMIN)
                        print("Catalogue sauvegardé.")
                case 3:
                    print("\n=== Ajout d'un album ===")
                    id_artiste = input("ID de l'artiste : ").strip()
                    resultats = label.rechercher_artiste(catalogue, "id", id_artiste)
                    if not resultats:
                        print("Artiste introuvable.")
                    else:
                        print(f"Artiste trouvé : {resultats[0]['nom']}")
                        try:
                            album = label.saisir_infos_album()
                            catalogue = label.ajouter_album(catalogue, id_artiste, album)
                            label.sauvegarder_catalogue(catalogue, CHEMIN)
                            print("Catalogue sauvegardé.")
                        except ValueError:
                            print("Année ou streams invalides. Album non ajouté.")
                case 4:
                    sous_menu_4()
                    sous_choix = input("Votre sous-choix : ").strip().lower()
                    df = analyse.charger_en_dataframe(CHEMIN)
                    if df.empty:
                        print("Aucune donnée disponible.")
                    else:
                        match sous_choix:
                            case 'a':
                                print("\n=== Top 5 des artistes par nombre total de streams ===")
                                print(analyse.top_5_artistes_par_streams(df))
                            case 'b':
                                print("\n=== Moyenne des streams par genre musical ===")
                                print(analyse.moyenne_streams_par_genre(df))
                            case 'c':
                                print("\n=== Nombre d'albums sortis par année ===")
                                print(analyse.nombre_de_albums_par_annee(df))
                            case 'd':
                                analyse.exporter_rapport_complet(df)
                            case _:
                                print("Sous-choix invalide.")
                case 5:
                    print("Au revoir !")
                case _:
                    print("Choix invalide. Entrez un nombre entre 1 et 5.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
        except FileNotFoundError:
            print(f"Fichier {CHEMIN} introuvable.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgramme interrompu.")
