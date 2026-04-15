import json 
import os
def charger_catalogue(catalogue):
   with open(catalogue, "r", encoding="utf-8") as f:
     return json.load(f)

def sauvegarder_catalogue(data, chemin):
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def lister_artistes(catalogue):
    for artiste in catalogue:
        print(f"ID: {artiste['id']} | Nom: {artiste['nom']} | Genre: {artiste['genre']} | Pays: {artiste['pays']} | Albums: {len(artiste['albums'])}")

def rechercher_artiste(catalogue, critere, valeur):
    resultats = []
    for artiste in catalogue:
        if valeur.lower() in artiste[critere].lower():
            resultats.append(artiste)
    return resultats

def ajouter_artiste(catalogue, artiste):
    for a in catalogue:
        if a["id"] == artiste["id"]:
            print("Cet identifiant existe déjà !")
            return catalogue
    catalogue.append(artiste)
    print("Artiste ajouté avec succès !")
    return catalogue

def ajouter_album(catalogue, id_artiste, album):
    for artiste in catalogue:
        if artiste["id"] == id_artiste:
            artiste["albums"].append(album)
            print("Album ajouté avec succès !")
            return catalogue
    print("Artiste introuvable !")
    return catalogue