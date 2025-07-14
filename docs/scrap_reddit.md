# 📂 Fichiers de sortie générés par le scraping Reddit

Ce document décrit les fichiers de sortie produits par le script de scraping Reddit. Ces fichiers sont automatiquement créés et enregistrés dans un dossier horodaté lors de l'exécution de `run_scraper()`.

---

## 🔺 Emplacement des résultats

Les résultats sont enregistrés dans un sous-dossier :

```
results/reddit/scraping_YYYY-MM-DD/scraping_YYYY-MM-DD_HH-MM/
```

Chaque exécution crée un nouveau sous-dossier, horodaté à la minute près.

---

## 📃 `reddit_comments_YYYY-MM-DD_HH-MM.csv`

### Contenu :

Fichier principal contenant les commentaires Reddit extraits et filtrés selon les `keyword_conditions`.

### Colonnes :

* `Subreddit` : nom du subreddit d'origine
* `Labels` : catégories sémantiques détectées (ex : Divulgation, Tromperie)
* `Matched_Keywords` : mots-clés qui ont permis le classement
* `Post_Title` : titre du post Reddit
* `Comment` : contenu du commentaire
* `Date_Comment` : date du commentaire (format AAAA-MM-JJ)

### Exemple :

```
"ChatGPT","Divulgation;Confiance","disclose;ai","Les chatbots devraient-ils se révéler ?","Je savais pas que c'était un bot, ça m'a mis mal à l'aise.","2025-07-14"
```

---

## 🔍 `keywords_YYYY-MM-DD_HH-MM.txt`

Fichier listant **tous les mots-clés uniques** extraits des `keyword_conditions` du fichier de configuration.

### Intérêt :

* Permet une vérification rapide des mots-clés utilisés lors du scraping.

### Exemple :

```
bot
chatbot
transparency
manipulated
...
```

---

## 🔢 `subreddits_YYYY-MM-DD_HH-MM.txt`

Contient la liste de tous les subreddits analysés pendant cette session.

### Exemple :

```
ChatGPT
Technology
AskReddit
...
```

---

## 📈 Post-Traitement automatique

Une fois les données extraites :

* Les doublons sont automatiquement supprimés du fichier CSV.
* Un log est écrit dans `scraper.log` à la racine du projet, incluant les subreddits réussis, ignorés ou interdits.

---

## ⚡ Récapitulatif

| Fichier                 | Description                               |
| ----------------------- | ----------------------------------------- |
| `reddit_comments_*.csv` | Données principales, commentaires classés |
| `keywords_*.txt`        | Tous les mots-clés utilisés               |
| `subreddits_*.txt`      | Subreddits visités                        |
| `scraper.log`           | Historique d'exécution                    |

Ces fichiers peuvent être exploités pour une analyse manuelle, une visualisation ou un traitement statistique ultérieur.
