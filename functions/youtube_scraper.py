from functions.get_youtube_comments import get_top_comments
from functions.utils import filter_and_save_comment
from functions.load_config import get_config
from functions.utils import is_good_language

config = get_config()
all_comments = {}

keyword_conditions = config["keyword_conditions"]

def scrap_youtube(file_path,video_ids, youtube, MAX_COMMENTS_PER_VIDEO):
    comments_found = 0

    for i, vid in enumerate(video_ids):
        print(f"🔎 Vidéo {i+1}/{len(video_ids)}: {vid}")

        try:
            # Récupérer le titre de la vidéo
            video_info = youtube.videos().list(
                part='snippet',
                id=vid
            ).execute()
            
            snippet = video_info['items'][0]['snippet']
            title = snippet['title']
            description = snippet.get('description', '')

            # 🔍 Vérification de la langue
            if not is_good_language(title + ' ' + description, config["youtube"]["language"]):
                print("⚠️ La langue de la vidéo n'est pas " + config["youtube"]["language"])
                continue  # 🔁 passe à la vidéo suivante

            # Récupérer les commentaires
            comments = get_top_comments(vid, MAX_COMMENTS_PER_VIDEO, youtube)
            print(f"✅ {len(comments)} commentaires récupérés")

            for comment in comments:
                comment_date = comment['publishedAt'][:10]
                comment_text = comment['textDisplay']
                comments_found += filter_and_save_comment(
                    source_name=vid,
                    comment_text=comment_text,
                    title=title,
                    date=comment_date,
                    keyword_conditions=keyword_conditions,
                    file_path=file_path
                )

        except Exception as e:
            print(f"⚠️ Erreur pour la vidéo {vid} : {e}")
            continue

    print(f"\n✅ Terminé : {comments_found} commentaires filtrés et sauvegardés.")
