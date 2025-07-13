import pandas as pd

def remove_duplicates_from_csv(file_path, output_path=None, subset_columns=None):
    """
    Supprime les doublons dans un CSV.

    Parameters:
    - file_path: Chemin du CSV d'entrée.
    - output_path: Chemin du CSV nettoyé (par défaut, réécrit dans le même fichier).
    - subset_columns: Liste des colonnes à utiliser pour identifier les doublons. Si None, toutes les colonnes sont utilisées.
    """
    
    print("Suppression des doublons...")
    
    df = pd.read_csv(file_path)

    # Nombre initial de lignes
    initial_count = len(df)

    # Suppression des doublons
    df_cleaned = df.drop_duplicates(subset=subset_columns, keep='first')

    # Nombre après suppression
    final_count = len(df_cleaned)
    removed = initial_count - final_count

    # Enregistrement du fichier nettoyé
    if output_path is None:
        output_path = file_path

    df_cleaned.to_csv(output_path, index=False, encoding='utf-8')

    print(f"✅ {removed} doublon(s) supprimé(s). Nouveau total : {final_count} lignes.")


