import json

def charger_catalogue(chemin):
    """Charge et retourne le JSON depuis le fichier."""
    with open(chemin, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder_catalogue(data, chemin):
    """Écrit les données dans le fichier JSON."""
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def lister_artistes(catalogue):
    """Retourne la liste des artistes avec infos résumés."""
    for artiste in catalogue:
        print(f"ID: {artiste['id']} | Nom: {artiste['nom']} | Genre: {artiste['genre']} | Pays: {artiste['pays']} | Albums: {len(artiste['albums'])}")

def rechercher_artiste(catalogue, critere, valeur):
    """Recherche par nom ou genre."""
    resultats = []
    for artiste in catalogue:
        if valeur.lower() in artiste[critere].lower():
            resultats.append(artiste)
    return resultats

def ajouter_artiste(catalogue, artiste):
    """Ajoute un artiste après validation."""
    for a in catalogue:
        if a["id"] == artiste["id"]:
            print("Cet identifiant existe déjà.")
            return catalogue
    catalogue.append(artiste)
    print("Artiste ajouté avec succès.")
    return catalogue

def ajouter_album(catalogue, id_artiste, album):
    """Ajoute un album à un artiste."""
    for artiste in catalogue:
        if artiste["id"] == id_artiste:
            artiste["albums"].append(album)
            print("Album ajouté avec succès.")
            return catalogue
    print("Artiste introuvable !")
    return catalogue

def afficher_detail_artiste(catalogue, id_artiste):
    """Affiche le détail d'un artiste avec la liste de ses albums."""
    for artiste in catalogue:
        if artiste["id"] == id_artiste:
            print(f"\nNom   : {artiste['nom']}")
            print(f"Genre : {artiste['genre']}")
            print(f"Pays  : {artiste['pays']}")
            print("\nAlbums :")
            for album in artiste["albums"]:
                print(f"  - {album['titre']} ({album['annee']}) | {album['streams']} streams")
            return
    print("Artiste introuvable.")

def saisir_infos_artiste():
    """Saisie interactive des informations d'un nouvel artiste."""
    print("\nSaisie d'un nouvel artiste")
    id_artiste = input("ID (ex: ART-013) : ").strip()
    nom = input("Nom : ").strip()
    genre = input("Genre : ").strip()
    pays = input("Pays : ").strip()
    return {
        "id": id_artiste,
        "nom": nom,
        "genre": genre,
        "pays": pays,
        "albums": []
    }

def verifier_identifiant(catalogue, id_artiste):
    """Retourne True si l'identifiant est disponible, False s'il existe déjà."""
    for artiste in catalogue:
        if artiste["id"] == id_artiste:
            return False
    return True

def saisir_infos_album():
    """Saisie interactive des informations d'un nouvel album."""
    print("\nSaisie d'un nouvel album")
    titre = input("Titre de l'album : ").strip()
    annee = int(input("Année de sortie : "))
    streams = int(input("Nombre de streams : "))
    return {
        "titre": titre,
        "annee": annee,
        "streams": streams
    }

def mettre_a_jour_catalogue(catalogue, chemin):
    """Sauvegarde le catalogue dans le fichier JSON."""
    sauvegarder_catalogue(catalogue, chemin)
    print("Catalogue mis à jour avec succès.")
    return catalogue
