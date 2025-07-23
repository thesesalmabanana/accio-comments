import requests

def get_tweets_by_keyword(query, max_results, language, bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    tweets = []
    next_token = None

    while len(tweets) < max_results:
        params = {
            "query": query + f" lang:{language} -is:retweet",
            "max_results": min(100, max_results - len(tweets)),
            "tweet.fields": "created_at,text,lang",
        }
        if next_token:
            params["next_token"] = next_token

        response = requests.get(
            "https://api.twitter.com/2/tweets/search/recent",
            headers=headers,
            params=params
        )

        if response.status_code != 200:
            print("Erreur API:", response.json())
            break

        data = response.json()
        new_tweets = data.get("data", [])
        tweets.extend(new_tweets)
        next_token = data.get("meta", {}).get("next_token")
        if not next_token:
            break

    return tweets
