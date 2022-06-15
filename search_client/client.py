from datetime import datetime
from typing import Optional

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
            "max_results": max_results,
        }

        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_tweet_info(self, tweet_id: str) -> dict:
        url = SearchClient.BASE_URL / "tweets" / tweet_id
        # ?expansions=attachments.media_keys&tweet.fields=created_at,author_id,lang,source,public_metrics,context_annotations,entities"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_tweets(
        self,
        query: list[str],
        *,
        max_results: int = 10,
        end_time: Optional[datetime] = None,
        start_time: Optional[datetime] = None,
        next_token: Optional[str] = None,
        since_id: Optional[str] = None,
        sort_order: Optional[str] = None,
        until_id: Optional[str] = None,
        expansions: Optional[list[str]] = None,
        media_fields: Optional[list[str]] = None,
        place_fields: Optional[list[str]] = None,
        poll_fields: Optional[list[str]] = None,
        tweet_fields: Optional[list[str]] = None,
        user_fields: Optional[list[str]] = None,
    ) -> dict:
        """
        Search recent tweets by separately providing query parameters.
        This method is meant to be lower-level and only abstracts making
        an actual HTTP request.

        Example:
        >>> sc = SearchClient("your_bearer_token")  # make SearchCLient obj
        >>> sc.get_tweets(query=["tesla", "from:elonmusk"])
        <Gives you 10 recent tweets with keyword "tesla" from elonmusk>

        >>> sc.get_tweets(query=["bitcoin", "from:elonmusk"], max_results=20)
        <Gives you 20 recent tweets with keyword "bitcoin" from elonmusk>

        Each parameter is described in the official documentation for Twitter API
        https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent

        Building low-level queries can be complicated at first.
        Make sure to read through the link below for understanding.
        https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
        """
        # preprocess query params
        query_val = " ".join(query)

        fields = {
            "media.fields": media_fields,
            "place.fields": place_fields,
            "poll.fields": poll_fields,
            "tweet.fields": tweet_fields,
            "user.fields": user_fields,
            "expansions": expansions,
        }
        field_params = {k: ",".join(v) for k, v in fields.items() if v}

        params = {
            **field_params,
            "query": query_val,
            "max_results": max_results,
            "end_time": end_time,
            "next_token": next_token,
            "since_id": since_id,
            "sort_order": sort_order,
            "start_time": start_time,
            "until_id": until_id,
        }
        url = SearchClient.BASE_URL / "tweets" / "search" / "recent"
        response = requests.get(url, params=params, headers=self.headers)
        return response.json()
