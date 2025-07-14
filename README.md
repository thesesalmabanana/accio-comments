# Accio‑Comments

**Accio‑Comments** est un outil Python permettant de **scraper des commentaires** selon des mots‑clés. 

---

## 🚀 Fonctionnalités

- Scraping complet de Reddit ou de subreddits spécifiques.
- Recherche de commentaires contenant des **mots‑clés** fournis.
- Sauvegarde des résultats dans des fichiers JSON ou CSV.
- Modularité grâce à un dossier `functions/` pour ajout de logiques personnalisées.

---

## ⚙️ Installation

1. Cloner ce dépôt :

   ```bash
   git clone https://github.com/thesesalmabanana/accio-comments.git
   cd accio-comments
   ```

2. (Optionnel) Créer un environnement virtuel recommandé :

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Installation des dépendances :

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

Une fois l'installation complète, il ne vous reste plus qu'à configurer votre **config.json**. 
Pour faire cela, [consultez la documentation](docs/config.md). 

---

## 🚀 Lancement du script principal

Pour exécuter l'application principale, il suffit de lancer la commande suivante dans votre terminal :

```bash
python run.py
```

Le script vous proposera un choix parmi différents programmes disponibles :

```text
Quel programme veux-tu lancer ?
1 - Scrap Reddit
2 - Scrap Youtube
Choix :
```

### 🔄 Fonctionnement du script `run.py`

* Le script sert de point d’entrée unique à l’application.
* Il affiche un menu interactif pour que l’utilisateur choisisse le module à exécuter.
* En fonction du choix (`1` ou `2`), il importe dynamiquement le bon module :

  * `scraps.scrap_reddit` pour scraper Reddit
  * `scraps.scap_youtube` pour scraper YouTube
* Ensuite, il appelle la fonction `run_scraper()` de ce module, qui lance le scraping.

Ce design permet d’organiser proprement plusieurs scripts indépendants tout en les pilotant via une interface centralisée.

