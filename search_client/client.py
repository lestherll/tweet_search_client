from __future__ import annotations

import datetime as dt
import time

import requests

from search_client.constants import config
from search_client.field_enums import MediaFields, PlaceFields, PollFields, TweetFields, UserFields
from search_client.url import URL


class SearchClient:

    BASE_URL: URL = URL(config.BASE_URL)

    def __init__(self, bearer_token: str) -> None:
        self.bearer_token = bearer_token
        self.headers = {"Authorization": f"Bearer {self.bearer_token}"}

    def get_user_id(self, username: str) -> str:
        url = SearchClient.BASE_URL / "users" / "by" / "username" / username
        response = requests.get(url, headers=self.headers)
        return response.json()["data"]["id"]

    def get_users(
        self,
        usernames: list[str],
        expansions: list[str] | None = None,
        tweet_fields: list[str] | None = None,
        user_fields: list[str] | None = None,
    ) -> dict:
        url = SearchClient.BASE_URL / "users" / "by"
        fields = {
            "usernames": [usernames] if isinstance(usernames, str) else usernames,
            "tweet.fields": tweet_fields,
            "user.fields": user_fields,
            "expansions": expansions,
        }
        params = {k: ",".join(v) for k, v in fields.items() if v}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_user(
        self,
        username: str,
        expansions: list[str] | None = None,
        tweet_fields: list[str] | None = None,
        user_fields: list[str] | None = None,
    ) -> dict:
        url = SearchClient.BASE_URL / "users" / "by" / "username" / username
        fields = {
            "tweet.fields": tweet_fields,
            "user.fields": user_fields,
            "expansions": expansions,
        }
        params = {k: ",".join(v) for k, v in fields.items() if v}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_tweets_by_user(
        self,
        user: str,
        max_results: int = 10,
    ) -> dict:
        user_id = self.get_user_id(user)
        url = SearchClient.BASE_URL / "users" / user_id / "tweets"

        params = {
            "tweet.fields": "created_at",
            # "expansions": "author_id"
            "max_results": max_results,
        }

        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_tweet_info(
        self,
        tweet_id: str | list[str],
        *,
        expansions: list[str] | None = None,
        media_fields: list[str] | None = None,
        place_fields: list[str] | None = None,
        poll_fields: list[str] | None = None,
        tweet_fields: list[str] | None = None,
        user_fields: list[str] | None = None,
    ) -> dict:
        url = SearchClient.BASE_URL / "tweets"
        # ?expansions=attachments.media_keys&tweet.fields=created_at,author_id,lang,source,public_metrics,context_annotations,entities"
        fields = {
            "ids": [tweet_id] if isinstance(tweet_id, str) else tweet_id,
            "media.fields": media_fields,
            "place.fields": place_fields,
            "poll.fields": poll_fields,
            "tweet.fields": tweet_fields,
            "user.fields": user_fields,
            "expansions": expansions,
        }
        params = {k: ",".join(v) for k, v in fields.items() if v}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def _get_tweet(
        self,
        query: list[str],
        *,
        max_results: int = 10,
        end_time: dt.datetime | None = None,
        start_time: dt.datetime | None = None,
        next_token: str | None = None,
        since_id: str | None = None,
        sort_order: str | None = None,
        until_id: str | None = None,
        expansions: list[str] | None = None,
        media_fields: list[str] | None = None,
        place_fields: list[str] | None = None,
        poll_fields: list[str] | None = None,
        tweet_fields: list[str] | None = None,
        user_fields: list[str] | None = None,
        archive: bool = False,
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
        url = SearchClient.BASE_URL / "tweets" / "search" / ("all" if archive else "recent")
        response = requests.get(url, params=params, headers=self.headers)
        return response.json()

    def get_all_tweets(
        self,
        query: list[str],
        *,
        cooldown: float = 3,
        max_results: int = 10,
        end_time: dt.datetime | None = None,
        start_time: dt.datetime | None = None,
        next_token: str | None = None,
        since_id: str | None = None,
        sort_order: str | None = None,
        until_id: str | None = None,
        expansions: list[str] | None = None,
        media_fields: list[str] | None = None,
        place_fields: list[str] | None = None,
        poll_fields: list[str] | None = None,
        tweet_fields: list[str] | None = None,
        user_fields: list[str] | None = None,
        tweet_only: bool = False,
        max_page: int | None = 1,
    ) -> dict | list:
        result = []
        params = {
            "max_results": max_results,
            "end_time": end_time,
            "start_time": start_time,
            "next_token": next_token,
            "since_id": since_id,
            "sort_order": sort_order,
            "until_id": until_id,
            "expansions": expansions,
            "media_fields": media_fields,
            "place_fields": place_fields,
            "poll_fields": poll_fields,
            "tweet_fields": tweet_fields,
            "user_fields": user_fields,
        }
        # tweets = self._get_tweet(query, **params, archive=True)

        while max_page is None or max_page > 0:
            tweets = self._get_tweet(query, **params, archive=True)

            if not tweets.get("data"):
                break

            if tweet_only:
                result.extend(tweets["data"])
            else:
                result.append(tweets)

            if max_page is not None:
                max_page -= 1

            params["next_token"] = tweets.get("meta").get("next_token")

            # check for max_page to eliminate waiting
            # when remaining page is 0 (max_page <= 0)
            if not params["next_token"] or (max_page is not None and max_page <= 0):
                break

            time.sleep(cooldown)

        return result

    def get_recent_tweets(
        self,
        query: list[str],
        *,
        cooldown: float = 3,
        max_results: int = 10,
        end_time: dt.datetime | None = None,
        start_time: dt.datetime | None = None,
        next_token: str | None = None,
        since_id: str | None = None,
        sort_order: str | None = None,
        until_id: str | None = None,
        expansions: list[str] | None = None,
        media_fields: list[str] | None = None,
        place_fields: list[str] | None = None,
        poll_fields: list[str] | None = None,
        tweet_fields: list[str] | None = None,
        user_fields: list[str] | None = None,
        tweet_only: bool = False,
        max_page: int | None = 1,
    ) -> dict | list:
        result = []
        params = {
            "max_results": max_results,
            "end_time": end_time,
            "start_time": start_time,
            "next_token": next_token,
            "since_id": since_id,
            "sort_order": sort_order,
            "until_id": until_id,
            "expansions": expansions,
            "media_fields": media_fields,
            "place_fields": place_fields,
            "poll_fields": poll_fields,
            "tweet_fields": tweet_fields,
            "user_fields": user_fields,
        }
        # tweets = self._get_tweet(query, **params, archive=False)

        while max_page is None or max_page > 0:
            tweets = self._get_tweet(query, **params, archive=False)

            if tweet_only:
                result.extend(tweets["data"])
            else:
                result.append(tweets)

            if max_page is not None:
                max_page -= 1

            params["next_token"] = tweets.get("meta").get("next_token")

            # check for max_page to eliminate waiting
            # when remaining page is 0 (max_page <= 0)
            if not params["next_token"] or (max_page is not None and max_page <= 0):
                break

            time.sleep(cooldown)

        return result

    def get_tweet_count_user(self, username: str, *, cooldown: float = 3) -> int:
        """Return total number of tweets from a user using username (twitter handle)

        Args:
            username (str): Twitter handle of the user ie username

        Returns:
            int: number of tweets they have tweeted since the creation of their account
        """
        url = SearchClient.BASE_URL / "tweets" / "counts" / "all"
        user = self.get_user(username, user_fields=[UserFields.CREATED_AT])
        query = f"from:{username}"
        start_time = user["data"]["created_at"]

        # we're subtracting 1 minute because end time must be less than 10 seconds
        # prior to the time the request was made according to Twitter API
        end_time = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=1)).isoformat()
        params = {
            "query": query,
            "start_time": start_time,
            "end_time": end_time,
            "granularity": "day",
        }
        total = 0
        while True:
            response = requests.get(url, headers=self.headers, params=params)
            meta = response.json().get("meta")
            total += meta.get("total_tweet_count")
            next_token = meta.get("next_token")
            if next_token:
                params["next_token"] = next_token
                time.sleep(cooldown)
            else:
                break
        return total

    def get_tweet_count(
        self,
        query: list[str],
        *,
        end_time: dt.datetime | None = None,
        start_time: dt.datetime | None = None,
        next_token: str | None = None,
        since_id: str | None = None,
        until_id: str | None = None,
        cooldown: float = 3,
    ) -> int:
        params = {
            "query": " ".join(query),
            "end_time": end_time,
            "granularity": "day",
            "next_token": next_token,
            "since_id": since_id,
            "start_time": start_time,
            "until_id": until_id,
        }

        url = SearchClient.BASE_URL / "tweets" / "counts" / "all"

        total = 0
        while True:
            response = requests.get(url, headers=self.headers, params=params)
            meta = response.json().get("meta")
            total += meta.get("total_tweet_count")
            next_token = meta.get("next_token")
            if next_token:
                params["next_token"] = next_token
                time.sleep(cooldown)
            else:
                break
        return total
