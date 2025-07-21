# 📁 Structure du fichier de configuration : `config.json.example`

Ce document décrit la structure du fichier `config.json.example`, un modèle que vous pouvez copier et adapter (`cp config.json.example config.json`) pour vos propres besoins.  
Le fichier réel `config.json` doit être ajouté au `.gitignore` pour éviter d'exposer des informations sensibles (identifiants API, mots-clés, etc.) dans votre dépôt Git.

---

## 🔑 `reddit_api`

Contient les identifiants d’API Reddit, nécessaires pour l’authentification avec Reddit via PRAW.

```json
"reddit_api": {
  "client_id": "your_client_id_here",
  "client_secret": "your_client_secret_here",
  "user_agent": "your_user_agent_name"
}
```

- `client_id` : fourni lors de l'enregistrement de votre application Reddit.
- `client_secret` : la clé secrète liée à l'application.
- `user_agent` : une chaîne d'identification personnalisée (ex. : `"myredditbot/1.0"`).

---

## 📺 `google_api`

Contient les identifiants nécessaires pour accéder à l'API YouTube Data via Google Cloud Platform.

```json
"google_api": {
  "api_key": "your_api_key_here",
  "service_name": "your_service_name_here",
  "api_version": "v3"
}
```

- `api_key` : clé API fournie par Google.
- `service_name` : généralement `"youtube"`.
- `api_version` : généralement `"v3"`.

---

## 🔍 `youtube`

Définit les paramètres de recherche et d'extraction pour les commentaires YouTube.

```json
"youtube": {
  "search_term": "your_search_term_here",
  "max_videos": 10,
  "max_comments_per_video": 100,
  "language": "en"
}
```

- `search_term` : terme de recherche utilisé dans YouTube.
- `max_videos` : nombre maximum de vidéos à analyser.
- `max_comments_per_video` : nombre maximum de commentaires à récupérer par vidéo.
- `language` : code de langue ISO (ex. `"en"` pour l’anglais).

---

## 📅 `subreddits`

Liste des subreddits à analyser (sans le `/r/`).

```json
"subreddits": [
  "ExampleSubreddit1",
  "ExampleSubreddit2"
]
```

- Chaque nom doit correspondre exactement à celui utilisé sur Reddit.

---

## 🧠 `keyword_conditions`

Définit les conditions de correspondance par mots-clés pour catégoriser les commentaires.

```json
"keyword_conditions": {
  "ExampleCategory": [
    ["base_term_1", "base_term_2"],
    ["specific_pattern_1", "specific_pattern_2"]
  ],
  "AnotherCategory": [
    ["ai", "bot"],
    ["trust", "misleading", "confused"]
  ]
}
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

Liste des noms d’utilisateurs Reddit connus comme étant des bots, à **ignorer** automatiquement lors du traitement.

```json
"knowBots": [
  "examplebot1",
  "examplebot2"
]
```

---

## 📚 Exemple complet de fichier `config.json.example`

```json
{
  "reddit_api": {
    "client_id": "your_client_id_here",
    "client_secret": "your_client_secret_here",
    "user_agent": "your_user_agent_name"
  },
  "google_api": {
    "api_key": "your_api_key_here",
    "service_name": "youtube",
    "api_version": "v3"
  },
  "youtube": {
    "search_term": "your_search_term_here",
    "max_videos": 10,
    "max_comments_per_video": 100,
    "language": "en"
  },
  "subreddits": [
    "ExampleSubreddit1",
    "ExampleSubreddit2"
  ],
  "keyword_conditions": {
    "ExampleCategory": [
      ["base_term_1", "base_term_2"],
      ["specific_pattern_1", "specific_pattern_2"]
    ],
    "AnotherCategory": [
      ["ai", "bot"],
      ["trust", "misleading", "confused"]
    ]
  },
  "knowBots": [
    "examplebot1",
    "examplebot2"
  ]
}
```

---

## 📌 Astuces

- Ajoutez le fichier réel `config.json` à votre `.gitignore` :

```bash
# .gitignore
config.json
```

- Pour l’utiliser :

```bash
cp config.json.example config.json
```

Et remplissez-le avec vos propres informations.
