from functions.get_x_posts import get_tweets_by_keyword
from functions.x_scraper import scrap_x
from functions.load_config import get_config
from functions.utils import init_csv
from functions.clear_csv import remove_duplicates_from_csv

def run_scraper():
    config = get_config()

    BEARER_TOKEN = config["twitter"]["bearer_token"]
    QUERY = config["twitter"]["search_term"]
    MAX_TWEETS = config["twitter"]["max_tweets"]
    LANGUAGE = config["twitter"]["language"]
    keyword_conditions = config["keyword_conditions"]

    tweet_data = get_tweets_by_keyword(QUERY, MAX_TWEETS, LANGUAGE, BEARER_TOKEN)
    file_path = init_csv("x", keyword_conditions)
    scrap_x(file_path, tweet_data, keyword_conditions, LANGUAGE)
    remove_duplicates_from_csv(file_path)