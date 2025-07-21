from googleapiclient.discovery import build

from functions.youtube_scraper import scrap_youtube
from functions.get_youtube_videos import get_video_ids
from functions.load_config import get_config
from functions.utils import init_csv
from functions.clear_csv import remove_duplicates_from_csv


def run_scraper():
    config = get_config()

    # 🔐 Ta clé API YouTube (à remplacer par la tienne)
    API_KEY = config["google_api"]["api_key"]
    YOUTUBE_API_SERVICE_NAME = config["google_api"]["service_name"]
    YOUTUBE_API_VERSION = config["google_api"]["api_version"]
    
    keyword_conditions = config["keyword_conditions"]

    # 🔍 Terme de recherche
    QUERY = config["youtube"]["search_term"]
    MAX_VIDEOS = config["youtube"]["max_videos"]
    MAX_COMMENTS_PER_VIDEO = config["youtube"]["max_comments_per_video"]
    LANGUAGE = config["youtube"]["language"]
    
    # Initialisation du client YouTube
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    # 🧠 Exécution
    video_ids = get_video_ids(QUERY, MAX_VIDEOS, youtube, LANGUAGE)
    
    # ➕ Création du fichier CSV
    file_path = init_csv("youtube", keyword_conditions, video_ids)
    
    scrap_youtube(file_path, video_ids, youtube, MAX_COMMENTS_PER_VIDEO)
    
    # Suppression des doublons
    remove_duplicates_from_csv(file_path)