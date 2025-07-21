import time

def get_top_comments(video_id, max_comments, youtube):
    comments = []
    next_page_token = None

    while len(comments) < max_comments:
        try:
            response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                maxResults=min(100, max_comments - len(comments)),
                order='relevance',
                textFormat='plainText',
                pageToken=next_page_token
            ).execute()

            for item in response['items']:
                snippet = item['snippet']['topLevelComment']['snippet']
                comment_text = snippet['textDisplay']
                comment_date = snippet['publishedAt'][:10]

                comments.append({
                    'textDisplay': comment_text,
                    'publishedAt': comment_date
                })

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        except Exception as e:
            print(f"Erreur pour la vidéo {video_id} : {e}")
            break

        time.sleep(1)  # Anti-throttling

    return comments
