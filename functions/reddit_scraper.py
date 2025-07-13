import logging
import praw
import prawcore
from tqdm import tqdm
from datetime import datetime
import time

# ========== IMPORTS CUSTOMS FUNCTIONS ==========
from functions.load_config import get_config
from functions.check_bots import is_bot
from functions.text_detection import match_keywords


# ========== LOAD CONFIG ==========
config = get_config()

# ========== REDDIT CONNECTION ==========
reddit = praw.Reddit(
    client_id=config["reddit_api"]["client_id"],
    client_secret=config["reddit_api"]["client_secret"],
    user_agent=config["reddit_api"]["user_agent"],
)


# ========== KEYWORD CONDITIONS (AND/OR STRUCTURE) ==========
keyword_conditions = config["keyword_conditions"]

def scrap_subreddit(subreddit_name, file_path):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        logging.info(f"🔎 Extraction des commentaires dans r/{subreddit_name}...")
        submissions = list(subreddit.hot(limit=500))
        comments_found = 0

        for submission in tqdm(submissions, desc=f"📄 {subreddit_name}", leave=False, ncols=100):
            if submission.num_comments == 0:
                continue

            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                comment_date = datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d')
                clean_comment = comment.body.replace('"', "'").replace(',', ' ')
                clean_title = submission.title.replace('"', "'").replace(',', ' ')

                if is_bot(comment):
                    continue

                labels, matched_keywords = match_keywords(comment.body, keyword_conditions)
                if labels:
                    clean_keywords = ';'.join(matched_keywords)
                    with open(file_path, mode='a', encoding='utf-8', newline='') as f:
                        f.write(f'"{subreddit_name}","{";".join(labels)}","{clean_keywords}","{clean_title}","{clean_comment}","{comment_date}"\n')
                    comments_found += 1

        tqdm.write(f"✅ Terminé r/{subreddit_name} : {comments_found} commentaires trouvés.")
        logging.info(f"✅ Terminé r/{subreddit_name} : {comments_found} commentaires trouvés.")

    except prawcore.exceptions.Redirect:
        tqdm.write(f"🚫 Subreddit inconnu ou banni: {subreddit_name}")
    except prawcore.exceptions.Forbidden:
        tqdm.write(f"🔒 Accès interdit à: {subreddit_name}")
    except prawcore.exceptions.TooManyRequests as e:
        wait_time = int(e.response.headers.get("Retry-After", 60))
        tqdm.write(f"⚠️  Trop de requêtes sur {subreddit_name}. Attente {wait_time}s...")
        time.sleep(wait_time)
        scrap_subreddit(subreddit_name, file_path)
    except Exception as e:
        logging.exception(f"❌ Erreur avec {subreddit_name}: {str(e)}")
    