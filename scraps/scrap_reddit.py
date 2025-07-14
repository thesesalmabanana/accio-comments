import os
import time
import logging
from tqdm import tqdm

# ========== IMPORTS CUSTOMS FUNCTIONS ==========
from functions.clear_csv import remove_duplicates_from_csv
from functions.reddit_scraper import scrap_subreddit
from functions.load_config import get_config

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

    # ========== PATHS ==========
    today = time.strftime("%Y-%m-%d")
    today_with_min = time.strftime("%Y-%m-%d_%H-%M")
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    folder_name = f"results/reddit/scraping_{today}"
    subfolder_name = f"scraping_{today_with_min}"
    subfolder_path = os.path.join(BASE_DIR, "..", folder_name, subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)

    # Fichiers
    file_path = os.path.join(subfolder_path, f"reddit_comments_{today_with_min}.csv")
    keywords_file_path = os.path.join(subfolder_path, f"keywords_{today_with_min}.txt")
    subreddits_file_path = os.path.join(subfolder_path, f"subreddits_{today_with_min}.txt")

    # ========== WRITE HEADERS ==========
    with open(file_path, mode='w', encoding='utf-8', newline='') as f:
        f.write("Subreddit,Labels,Matched_Keywords,Post_Title,Comment,Date_Comment\n")

    with open(subreddits_file_path, mode='w', encoding='utf-8') as f:
        f.write('\n'.join(subreddits))

    unique_keywords = set()

    for group in keyword_conditions.values():
        for keyword_list in group:
            unique_keywords.update(keyword_list)

    with open(keywords_file_path, mode='w', encoding='utf-8') as f:
        for keyword in sorted(unique_keywords):
            f.write(f"{keyword}\n")

    # ========== MAIN ==========
    for subreddit_name in tqdm(subreddits, desc="🔎 Scraping Subreddits", ncols=100):
        scrap_subreddit(subreddit_name, file_path)

    final_msg = f"✅ Extraction terminée. Fichier sauvegardé ici : {file_path}"
    print(final_msg)
    logging.info(final_msg)

    # Suppression des doublons
    remove_duplicates_from_csv(file_path)
