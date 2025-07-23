from functions.utils import is_good_language, filter_and_save_comment

def scrap_x(file_path, tweets, keyword_conditions, target_language):
    comments_found = 0

    for tweet in tweets:
        text = tweet["text"]
        tweet_id = tweet["id"]
        date = tweet["created_at"][:10]

        if not is_good_language(text, target_language):
            continue

        comments_found += filter_and_save_comment(
            source_name=tweet_id,
            comment_text=text,
            title="-",
            date=date,
            keyword_conditions=keyword_conditions,
            file_path=file_path
        )

    print(f"✅ Terminé : {comments_found} tweets filtrés et sauvegardés.")
