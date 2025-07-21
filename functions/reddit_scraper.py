import logging
import praw
import prawcore
from tqdm import tqdm
from datetime import datetime
import time

# ========== IMPORTS CUSTOMS FUNCTIONS ==========
from functions.load_config import get_config
from functions.check_bots import is_bot
from functions.utils import filter_and_save_comment

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
                if is_bot(comment):
                    continue

                comment_date = datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d')
                comments_found += filter_and_save_comment(
                    source_name=subreddit_name,
                    comment_text=comment.body,
                    title=submission.title,
                    date=comment_date,
                    keyword_conditions=keyword_conditions,
                    file_path=file_path
                )


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
    