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

# 🔹 Liste des subreddits à analyser
subreddits = ["Chatbots", "artificial", "AIethics","MachineLearning"]  # Ajoute d'autres subreddits ici
# Mots-clés à filtrer
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
    "chatbot lying about being human"
]
max_posts = 50  # Nombre de posts analysés par subreddit

# 🔹 Chargement du modèle BERT pour l'analyse de sentiment
bert_model = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_pipeline = pipeline("sentiment-analysis", model=bert_model)

# 🔹 Chargement du tokenizer BERT pour tronquer proprement les longs commentaires
tokenizer = AutoTokenizer.from_pretrained(bert_model)

# 🔹 Préparation du traitement NLP
nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download("stopwords")
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    """ Nettoie le texte : minuscule, suppression de la ponctuation, tokenisation, lemmatisation """
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)

def truncate_text(text, max_tokens=510):
    """ Tronque le texte proprement en utilisant le tokenizer de BERT """
    tokens = tokenizer.tokenize(text)
    truncated_tokens = tokens[:max_tokens]
    return tokenizer.convert_tokens_to_string(truncated_tokens)

# 📌 Étape 2 : Récupération des commentaires
comments_data = []

for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    print(f"🔎 Extraction des commentaires dans r/{subreddit_name}...")

    for submission in subreddit.hot(limit=max_posts):  # Analyse les top posts
        submission.comments.replace_more(limit=0)  # Charge tous les commentaires

        for comment in submission.comments.list():
            if any(keyword.lower() in comment.body.lower() for keyword in keywords):
                truncated_comment = truncate_text(comment.body)  # Tronquer avant BERT
                processed_comment = preprocess_text(comment.body)  # Nettoyage du texte
                
                # Analyse de sentiment avec BERT
                sentiment = sentiment_pipeline(truncated_comment)[0]['label']
                
                comments_data.append([subreddit_name, submission.title, comment.body, processed_comment, sentiment])

# 📌 Étape 3 : Création du DataFrame
df = pd.DataFrame(comments_data, columns=["Subreddit", "Post_Title", "Comment", "Processed_Comment", "BERT_Sentiment"])

# 📌 Étape 4 : Sauvegarde des résultats
df.to_csv("reddit_comments_multiple_subs.csv", index=False, encoding="utf-8")
print("✅ Extraction et analyse terminées ! Résultats enregistrés dans reddit_comments_multiple_subs.csv")

# 📌 Étape 5 : Visualisation
plt.figure(figsize=(8, 5))
sns.countplot(x=df["BERT_Sentiment"], hue=df["Subreddit"], palette="coolwarm")
plt.title("Analyse de Sentiment des Commentaires Reddit (BERT)")
plt.xlabel("Sentiment")
plt.ylabel("Nombre de commentaires")
plt.legend(title="Subreddit")
plt.show()