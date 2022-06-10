import requests
from constants import config
from url import URL


class SearchClient:

    BASE_URL: URL = URL(config.BASE_URL)

    def __init__(self, bearer_token: str) -> None:
        self.bearer_token = bearer_token
        self.headers = {"Authorization": f"Bearer {self.bearer_token}"}

    def get_user_id(self, username: str) -> str:
        url = SearchClient.BASE_URL / "users" / "by" / "username" / username
        response = requests.get(url, headers=self.headers)
        return response.json()["data"]["id"]

    def get_tweets_by_user(self, user: str, max_results: int = 10) -> dict:
        user_id = self.get_user_id(user)
        url = SearchClient.BASE_URL / "users" / user_id / "tweets"
        
        params = {
            "tweet.fields": "created_at",
            # "expansions": "author_id"
            "max_results": max_results
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_tweet_info(self, tweet_id: str) -> dict:
        url = SearchClient.BASE_URL / "tweets" /tweet_id
        # ?expansions=attachments.media_keys&tweet.fields=created_at,author_id,lang,source,public_metrics,context_annotations,entities"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_tweets(self, *keywords: str) -> dict:
        """
        Twitter API query is different, all query must go into
        one query `key` for the lack of a better word. Returns
        tweets based on keywords provided.
        """
        query = " ".join(keywords)
        params = {"query": query}
        url = SearchClient.BASE_URL / "tweets" / "search" / "recent"
        response = requests.get(url, params=params, headers=self.headers)
        return response.json()
