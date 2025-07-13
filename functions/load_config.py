import json
import os

# Obtenir le chemin absolu du dossier contenant ce fichier (load_config.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construire le chemin vers config.json basé sur la position réelle du script
file_path = os.path.join(BASE_DIR, "..", "config.json")

def get_config():
    with open(file_path, 'r') as f:
        return json.load(f)