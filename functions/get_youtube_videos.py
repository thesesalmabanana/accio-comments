def get_video_ids(query, max_results, youtube):
    video_ids = []
    next_page_token = None

    while len(video_ids) < max_results:
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id',
            maxResults=min(50, max_results - len(video_ids)),
            pageToken=next_page_token
        ).execute()

        for item in search_response['items']:
            video_ids.append(item['id']['videoId'])

        next_page_token = search_response.get('nextPageToken')
        if not next_page_token:
            break

    return video_ids