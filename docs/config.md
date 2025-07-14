# 📁 Structure du fichier de configuration : `config.json.example`

Ce document explique la structure attendue et le rôle de chaque champ dans le fichier `config.json.example`. Vous pouvez utiliser ce modèle comme point de départ, le renommer en `config.json` et y insérer vos propres identifiants et préférences. Le fichier réel `config.json` doit être ajouté au `.gitignore` afin de ne pas exposer de données sensibles dans le contrôle de version.

---

## 🔑 `reddit_api`

Contient les identifiants d'API Reddit. Ces informations sont nécessaires pour s'authentifier auprès de l'API Reddit.

```json
"reddit_api": {
  "client_id": "votre_client_id_ici",
  "client_secret": "votre_client_secret_ici",
  "user_agent": "votre_user_agent_personnalisé"
}
```

* `client_id` : fourni par Reddit lors de l'enregistrement de votre application.
* `client_secret` : clé secrète donnée par Reddit.
* `user_agent` : chaîne courte identifiant votre script (ex. : `monbotreddit/1.0`).

---

## 📅 `subreddits`

Liste des noms de subreddits (sans le `/r/`) à analyser.

```json
"subreddits": [
  "ChatGPT",
  "ArtificialIntelligence",
  "OpenAI"
]
```

* Chaque élément est un nom de subreddit tel qu’il apparaît dans l’URL.

---

## 🔍 `keyword_conditions`

Définit des catégories sémantiques à partir de **deux listes de mots-clés**.
Chaque catégorie est associée à une liste de **deux tableaux** :

```json
"NomCategorie": [
  ["mot_base_1", "mot_base_2"],
  ["expression_specifique_1", "expression_specifique_2"]
]
```

### 🧠 Correspondance logique

Pour qu’un post soit classé dans une catégorie :

> Il doit contenir **au moins un mot** de la première liste **ET** **au moins un mot** de la deuxième liste.

### 🔎 Exemple

```json
"Divulgation": [
  ["chatbot", "ai"],
  ["disclose", "transparency"]
]
```

Si un post contient par exemple :

> "Je pense que le chatbot devrait être plus transparent."

Il sera classé dans la catégorie `Divulgation`.

### 📊 Remarques

* Les deux listes sont obligatoires.
* La correspondance est insensible à la casse (recommandé).
* Vous pouvez définir autant de catégories que nécessaire.

---

## 🤖 `knowBots`

Liste des bots Reddit connus à ignorer pendant l'analyse.

```json
"knowBots": [
  "automoderator",
  "remindmebot",
  "gpt2bot"
]
```

* Cela permet d’éliminer les bruits causés par les messages automatiques.

---

## 📚 Exemple de fichier : `config.json.example`

```json
{
  "reddit_api": {
    "client_id": "votre_client_id_ici",
    "client_secret": "votre_client_secret_ici",
    "user_agent": "votre_user_agent"
  },
  "subreddits": [
    "ChatGPT",
    "ArtificialIntelligence",
    "OpenAI"
  ],
  "keyword_conditions": {
    "Divulgation": [
      ["chatbot", "ai"],
      ["disclose", "transparency"]
    ],
    "Tromperie": [
      ["chatbot", "ai"],
      ["lie", "manipulate"]
    ]
  },
  "knowBots": [
    "automoderator",
    "remindmebot"
  ]
}
```

---

## 📌 Astuces

* Ajoutez le vrai fichier `config.json` au `.gitignore` pour ne pas l’ajouter au dépôt Git :

```bash
# .gitignore
config.json
```

* Pour l’utiliser :

```bash
cp config.json.example config.json
```

Et remplissez-le avec vos propres informations.

Si vous souhaitez un script Python pour valider automatiquement la structure de ce fichier, faites-moi signe !
