import os
import time
import logging
from tqdm import tqdm

# ========== IMPORTS CUSTOMS FUNCTIONS ==========
from functions.clear_csv import remove_duplicates_from_csv
from functions.reddit_scraper import scrap_subreddit
from functions.load_config import get_config
from functions.utils import init_csv

def run_scraper():
    # ========== LOGGING ==========
    logging.basicConfig(
        filename='scraper.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    config = get_config()

    # ========== SUBREDDITS ==========
    subreddits = config["subreddits"]

    # ========== KEYWORD CONDITIONS (AND/OR STRUCTURE) ==========
    keyword_conditions = config["keyword_conditions"]

    # ========== INIT CSV ==========
    file_path = init_csv("reddit", keyword_conditions, subreddits)    

    # ========== MAIN ==========
    for subreddit_name in tqdm(subreddits, desc="🔎 Scraping Subreddits", ncols=100):
        scrap_subreddit(subreddit_name, file_path)

    final_msg = f"✅ Extraction terminée. Fichier sauvegardé ici : {file_path}"
    print(final_msg)
    logging.info(final_msg)

    # Suppression des doublons
    remove_duplicates_from_csv(file_path)
