import os
import praw
import pandas as pd
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from transformers import pipeline, AutoTokenizer
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 Étape 1 : Configuration de l'API Reddit
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID_REDDIT"),
    client_secret=os.getenv("CLIENT_SECRET_REDDIT"),
    user_agent=os.getenv("USER_AGENT_REDDIT")
)

# 🔹 Définition des mots-clés à rechercher sur tout Reddit
keywords = [
    "chatbot" ,
    "pretending" ,
    "human",
    "AI pretending to be human",
    "chatbot deception",
    "chatbot human-like",
    "chatbot tricking users",
    "AI fooling people",
    "chatbot passes as human",
    "chatbot impersonation",
    "chatbot identity disclosure",
    "chatbot lying about being human",
    "chatbot trust issues",
    "chatbot ethical concerns",
    "AI deception",
    "chatbot misleading users",
    "chatbot lied to me",
    "chatbot manipulation",
    "chatbot faking identity",
    "I thought I was talking to a human",
    "chatbot fooled me",
    "chatbot tricked me",
    "I didn't know it was a chatbot",
    "chatbot didn't disclose its identity",
    "I realized it was a chatbot",
] # Ajoute d'autres mots-clés ici
max_posts = 30  # Nombre de posts à récupérer

# 🔹 Chargement du modèle BERT pour l'analyse de sentiment
# bert_model = "distilbert-base-uncased-finetuned-sst-2-english"
# sentiment_pipeline = pipeline("sentiment-analysis", model=bert_model)

# # 🔹 Chargement du tokenizer BERT pour tronquer proprement les longs commentaires
# tokenizer = AutoTokenizer.from_pretrained(bert_model)

# # 🔹 Préparation du traitement NLP
# nltk.download("punkt")
# nltk.download("stopwords")
# nltk.download("wordnet")
# lemmatizer = WordNetLemmatizer()
# stop_words = set(stopwords.words("english"))

# def preprocess_text(text):
#     """ Nettoie le texte : minuscule, suppression de la ponctuation, tokenisation, lemmatisation """
#     text = text.lower()
#     text = text.translate(str.maketrans("", "", string.punctuation))
#     tokens = word_tokenize(text)
#     tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
#     return " ".join(tokens)

# def truncate_text(text, max_tokens=512):
#     """ Tronque le texte proprement en utilisant le tokenizer de BERT """
#     tokens = tokenizer.tokenize(text)
#     truncated_tokens = tokens[:max_tokens]
#     return tokenizer.convert_tokens_to_string(truncated_tokens)

# 📌 Étape 2 : Recherche de posts sur tout Reddit
comments_data = []

for keyword in keywords:
    print(f"🔎 Recherche de posts contenant '{keyword}' sur Reddit...")

    for submission in reddit.subreddit("all").search(keyword, limit=max_posts):
        submission.comments.replace_more(limit=0)  # Charge tous les commentaires

        for comment in submission.comments.list():
            # truncated_comment = truncate_text(comment.body)  # Tronquer avant BERT
            # processed_comment = preprocess_text(comment.body)  # Nettoyage du texte
            
            # # Analyse de sentiment avec BERT
            # sentiment = sentiment_pipeline(truncated_comment)[0]['label']
            
            comments_data.append(
                [
                    submission.subreddit.display_name, 
                    submission.title, 
                    keyword, 
                    comment.body, 
                    # processed_comment, 
                    # sentiment
                ]
            )

# 📌 Étape 3 : Création du DataFrame
df = pd.DataFrame(
    comments_data, 
    columns=[
        "Subreddit", 
        "Post_Title", 
        "Keyword", 
        "Comment", 
        # "Processed_Comment", 
        # "BERT_Sentiment"
        ]
    )

# 📌 Étape 4 : Sauvegarde des résultats
df.to_csv("reddit_comments_global_search.csv", index=False, encoding="utf-8")
print("✅ Recherche et analyse terminées ! Résultats enregistrés dans reddit_comments_global_search.csv")

# # 📌 Étape 5 : Visualisation
# plt.figure(figsize=(8, 5))
# sns.countplot(x=df["BERT_Sentiment"], hue=df["Keyword"], palette="coolwarm")
# plt.title("Analyse de Sentiment des Commentaires Reddit (BERT)")
# plt.xlabel("Sentiment")
# plt.ylabel("Nombre de commentaires")
# plt.legend(title="Mot-clé")
# plt.show()
