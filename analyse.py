import pandas as pd
import os
from label import charger_catalogue

def charger_en_dataframe(chemin="catalogue.json"):
    """Charge le catalogue JSON et le convertit en DataFrame Pandas aplati."""
    try:
        data = charger_catalogue(chemin)
        df_artistes = pd.DataFrame(data)
        if df_artistes.empty:
            return pd.DataFrame()
        df = df_artistes.explode('albums', ignore_index=True)
        mask = df['albums'].notna()
        if mask.any():
            albums_df = pd.json_normalize(df.loc[mask, 'albums'])
            albums_df.index = df.loc[mask].index
            df = pd.concat([df.drop(columns=['albums']), albums_df], axis=1)
        else:
            df = df.drop(columns=['albums'])
        return df
    except Exception as e:
        print(f"Erreur de chargement : {e}")
        return pd.DataFrame()

def top_5_artistes_par_streams(df):
    """Retourne le top 5 des artistes par nombre total de streams."""
    if df.empty or 'nom' not in df.columns or 'streams' not in df.columns:
        return pd.DataFrame()
    return (
        df.groupby('nom')
        .agg(total_streams=('streams', 'sum'), nb_albums=('titre', 'count'))
        .nlargest(5, 'total_streams')
        .reset_index()
    )

def moyenne_streams_par_genre(df):
    """Retourne la moyenne des streams par genre musical."""
    if df.empty or 'genre' not in df.columns or 'streams' not in df.columns:
        return pd.DataFrame()
    return (
        df.groupby('genre')['streams']
        .mean()
        .round(0)
        .sort_values(ascending=False)
        .reset_index(name='moyenne_streams')
    )

def nombre_de_albums_par_annee(df):
    """Retourne le nombre d'albums sortis par année (agrégation)."""
    if df.empty or 'annee' not in df.columns:
        return pd.DataFrame()
    return (
        df.groupby('annee')
        .size()
        .reset_index(name='nombre_albums')
        .sort_values('annee')
    )

def exporter_rapport_complet(df, chemin="rapport.csv"):
    """Exporte le DataFrame complet dans un fichier CSV."""
    try:
        dir_name = os.path.dirname(chemin)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        df.to_csv(chemin, index=False, encoding='utf-8-sig')
        print(f"Rapport complet exporté avec succès : {chemin}")
    except Exception as e:
        print(f"Erreur lors de l'export : {e}")

if __name__ == "__main__":
    print("=== Test du module analyse.py ===")
    df = charger_en_dataframe()
    print(f"Nombre de lignes dans le DataFrame : {len(df)}")
    if not df.empty:
        print("\nColonnes disponibles :", list(df.columns))
        print("\nAperçu des 5 premières lignes :")
        print(df.head())
        print("\n=== Test Top 5 ===")
        print(top_5_artistes_par_streams(df))
    else:
        print("Le DataFrame est vide. Vérifie que catalogue.json existe.")
