import os
import time

from functions.text_detection import match_keywords

def filter_and_save_comment(source_name, comment_text, title, date, keyword_conditions, file_path):
    labels, matched_keywords = match_keywords(comment_text, keyword_conditions)
    if labels:
        clean_comment = comment_text.replace('"', "'").replace(',', ' ')
        clean_title = title.replace('"', "'").replace(',', ' ')
        clean_keywords = ';'.join(matched_keywords)

        with open(file_path, mode='a', encoding='utf-8', newline='') as f:
            f.write(f'"{source_name}","{";".join(labels)}","{clean_keywords}","{clean_title}","{clean_comment}","{date}"\n')
        return 1  # Comptabilisé
    return 0

def init_csv(platform, keyword_conditions, subreddits = ''):
    
    today = time.strftime("%Y-%m-%d")
    today_with_min = time.strftime("%Y-%m-%d_%H-%M")
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    folder_name = f"results/{platform.lower()}/scraping_{today}"
    subfolder_name = f"scraping_{today_with_min}"
    subfolder_path = os.path.join(BASE_DIR, "..", folder_name, subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)

    # Fichiers
    file_path = os.path.join(subfolder_path, f"{platform.lower()}_comments_{today_with_min}.csv")
    keywords_file_path = os.path.join(subfolder_path, f"keywords_{today_with_min}.txt")
    
    match platform.lower():
        case "reddit":
            subreddits_file_path = os.path.join(subfolder_path, f"subreddits_{today_with_min}.txt")
            with open(file_path, mode='w', encoding='utf-8', newline='') as f:
                f.write("Subreddit,Labels,Matched_Keywords,Post_Title,Comment,Date_Comment\n")
            with open(subreddits_file_path, mode='w', encoding='utf-8') as f:
                f.write('\n'.join(subreddits))
        case "youtube":
            with open(file_path, mode='w', encoding='utf-8', newline='') as f:
                f.write("Video_ID,Labels,Matched_Keywords,Video_Title,Comment,Date_Comment\n")

    # Keywords
    unique_keywords = set()

    for group in keyword_conditions.values():
        for keyword_list in group:
            unique_keywords.update(keyword_list)

    with open(keywords_file_path, mode='w', encoding='utf-8') as f:
        for keyword in sorted(unique_keywords):
            f.write(f"{keyword}\n")

    return file_path
