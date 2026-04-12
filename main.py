def menu():
 print("1 - Consulter le catalogue")
 print("2 - Ajouter un Article")
 print("3 - Ajouter un Album à un Artiste existant")
 print("4 - Statistiques et rapport")
 print("5 - Quitter l'application")

def sous_menu_1():
 print("a - Afficher tout les articles (nom, genre, pays, nombre d'album")
 print("b - Rechercher un artiste par nom ou par genre")
 print("c - Afficher le détail d'un artiste")

def sous_menu_2():
 print("a - Saisir les informations de l'artiste au clavier")
 print("b - Vérifier que l'identifiant n'existe pas déjà")
 print("c - Sauvegarder immédiatement dans catalogue.json")

def sous_menu_3():
 print("a - Rechercher l'artiste par son identifiant")
 print("b - Saisir les informations de l'album (titre, année, stream ) ")
 print("c - Mettre à jour catalogue.json")

def sous_menu_4():
 print("a - Top 5 des artistes par nombre total de streams")
 print("b - Moyenne des streams par genre musical")
 print("c - Nombre d'album sorti par année (agrégation)")
 print("d - Exporter le rapport complet dans rapport.csv")

def main():
 choix = 0
 print("Bienvenue dans mon application")
 while (choix !=5):
  menu()
  choix = int(input("Votre choix : "))
  match choix:
   case 1:
    sous_menu_1()
   case 2:
    sous_menu_2()
   case 3:
    sous_menu_3()
   case 4:
    sous_menu_4()
   case 5:
    exit
   case _:
    print("Mauvaise valeur")
if __name__=="__main__":
 try:
  main()
 except KeyboardInterrupt:
  print("Programme interrompu ...")