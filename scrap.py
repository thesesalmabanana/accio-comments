import praw
import pandas as pd
import prawcore
import os

# 1. Configuration de l'API Reddit
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID_REDDIT"),
    client_secret=os.getenv("CLIENT_SECRET_REDDIT"),
    user_agent=os.getenv("USER_AGENT_REDDIT")
)

# 2. Paramètres de recherche

subreddits = [ "Graphic_Design", "ArtificialInteligence", "AskReddit", "Futurology", "GetNoted", "Science", "YouShouldKnow", "Chatbots", "Artificial", "AIethics", "MachineLearning", "OpenAI", "AIChatGPT", "NonHumanIdentities", "AskReddit", "TrueOffMyChest","Technology", "Privacy", "Cybersecurity", "GoogleAssistant", "Alexa", "Siri", "CustomerService", "BotsRights", "ShittyRobots", "AIgonewild", "Computing", "DataScience", "InternetMysteries", "UXDesign", "Marketing", "AdTech","TechNews", "Deception", "AIandRobotic", "TalesFromTheCustomer", "TalesFromTechSupport", "RetailHell", "NoGoodCustomer" ]

keywords = [
    "chatbot",
    "pretending to be",
    "disclosure",
    "identity disclosure",
    "AI human",
    "deception",
    "human like",
    "tricking users",
    "fooling people",
    "passes as human",
    "impersonation",
    "lying about being human",
    "trust issues",
    "ethical concerns",
    "AI deception",
    "misleading users",
    "lied to me",
    "manipulation",
    "faking identity",
    "I thought I was talking to a human",
    "fooled me",
    "tricked me",
    "trust ai",
]

# 3. Récupération des derniers posts du subreddit

comments_data = []
for subreddit_name in subreddits:
    try:
        subreddit = reddit.subreddit(subreddit_name)
        print(f"🔎 Extraction des commentaires dans r/{subreddit_name}...")
        for submission in subreddit.hot(limit=50):  # Récupérer 50 posts populaires
            submission.comments.replace_more(limit=0)  # Charger tous les commentaires
            for comment in submission.comments.list():
                if any(keyword.lower() in comment.body.lower() for keyword in keywords):
                    print(submission.title)
                    comments_data.append([submission.title, comment.body])
    except prawcore.exceptions.Redirect:
        print(f"🚫 Subreddit inconnu ou banni lors de la recherche '{subreddit_name}'")
    except prawcore.exceptions.Forbidden:
        print(f"🔒 Accès interdit au subreddit")
    except Exception as e:
        print(f"❌ Erreur inattendue avec la recherche Reddit : {str(e)}")
        
# 4. Création d'un DataFrame Pandas
df = pd.DataFrame(comments_data, columns=["Post_Title", "Comment"])

# 5. Export en CSV pour traitement sous R
df.to_csv("reddit_comments.csv", index=False, encoding="utf-8")

print("Extraction terminée ! Fichier reddit_comments.csv créé.")
