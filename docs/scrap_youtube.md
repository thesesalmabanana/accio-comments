# 📂 Fichiers de sortie générés par le scraping YouTube

Ce document décrit les fichiers de sortie produits par le script de scraping YouTube. Ces fichiers sont automatiquement créés et enregistrés dans un dossier horodaté lors de l'exécution de `run_scraper()`.

---

## 🔺 Emplacement des résultats

Les résultats sont enregistrés dans un sous-dossier :

```
results/youtube/scraping_YYYY-MM-DD/scraping_YYYY-MM-DD_HH-MM/
```

Chaque exécution crée un nouveau sous-dossier, horodaté à la minute près.

---

## 📃 `youtube_comments_YYYY-MM-DD_HH-MM.csv`

### Contenu :

Fichier principal contenant les commentaires YouTube extraits et filtrés selon les `keyword_conditions`.

### Colonnes :

* `Video_ID` : identifiant unique de la vidéo YouTube
* `Labels` : catégories sémantiques détectées (ex : Technologie, Sentiment)
* `Matched_Keywords` : mots-clés qui ont permis le classement
* `Video_Title` : titre de la vidéo
* `Comment` : contenu du commentaire
* `Date_Comment` : date du commentaire (format AAAA-MM-JJ)

### Exemple :

```
"abc123","Technologie;IA","intelligence artificielle;machine learning","L'IA va-t-elle changer le monde ?","Je pense que l'IA va tout bouleverser.","2025-07-14"
```

---

## 🔍 `keywords_YYYY-MM-DD_HH-MM.txt`

Fichier listant **tous les mots-clés uniques** extraits des `keyword_conditions` du fichier de configuration.

### Intérêt :

* Permet une vérification rapide des mots-clés utilisés lors du scraping.

### Exemple :

```
intelligence artificielle
machine learning
nul
génial
...
```

---

## 📈 Post-Traitement automatique

Une fois les données extraites :

* Les doublons sont automatiquement supprimés du fichier CSV.
* Un log est affiché dans la console pour signaler les erreurs ou vidéos ignorées (langue incorrecte, etc.).

---

## ⚡ Récapitulatif

| Fichier                   | Description                               |
|---------------------------|-------------------------------------------|
| `youtube_comments_*.csv` | Données principales, commentaires classés |
| `keywords_*.txt`          | Tous les mots-clés utilisés               |

Ces fichiers peuvent être exploités pour une analyse manuelle, une visualisation ou un traitement statistique ultérieur.
