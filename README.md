# Twitter Search Client (WIP)
An unofficial **WIP** client for the twitter API that has only one goal; search for tweets.


# Installation
Package is not ready for PyPI yet but it can be installed directly from GitHub using `pip`.
```shell
pip install git+https://github.com/lestherll/twitter_search_client
```

# Setup and Prerequisites
Before everything, make sure that you have a developer account and a **bearer token** from Twitter. You can find out how to get one [here](https://developer.twitter.com/en/docs/twitter-api)

Project requires you to create a `.env` file at the project root. The library forces you to create one by default so that there is less risk in leaking your credentials accidentally.

`.env` file should look like below
```env
BEARER_TOKEN=your_bearer_token_that_you_got_from_twitter
```
The bearer token will be automatically passed to `search_client.constants.config` and can be accessed as such.
```py
from search_client.constants import config

print(config.BEARER_TOKEN)
```

In environments where creating a `.env` is not possible, you can just pass the bearer token directly to the `SearchClient` class. You must, however, be aware that you would be exposing your keys to others.
```py
from search_client import SearchClient


client = SearchClient("your_keys_must_be_string")

# do low-level work with client using /search/recent
tweets = client.get_recent_tweets(query=["from:twitterDev"])

# do low-level work with client using /search/all
tweets = client.get_all_tweets(query=["from:twitterDev"])

# do high-level work with client using /search/recent
tweets = client.get_tweets(
    query=["from:twitterDev"],
    number_of_tweets=10,
    archive=False,          # default is False which uses /recent
)

# do high-level work with client using /search/all
tweets = client.get_tweets(
    query=["from:twitterDev"],
    number_of_tweets=10,
    archive=True,           # archive must be set to True for /all
)
```

# Usage
[SearchClient](search_client/client.py) will be the interface exposed to the user. It will contain everything to do with searching tweets. It is  planned to use other endpoints of the Twitter API and expose them through other client types.

### Main endpoints supported
| Twitter API Endpoint              | Method                           | V2 Access Levels  |
|-----------------------------------|----------------------------------|-------------------|
| `/search/recent`                  | `SearchClient.get_recent_tweets` | Developer         |
| `/search/all`                     | `SearchClient.get_all_tweets`    | Academic          |
| `/search/all` or `/search/recent` | `SeachClient.get_tweets`         | Developer/Academic|
| `/tweets/counts/all`              | `SearchClient.get_tweet_counts`  | Academic          |

These methods are low-level wrappers (except for `get_tweets`) over raw requests to their respective endpoints. [Enumerations](./search_client/field_enums.py) are provided forconvenience of passing [fields](https://developer.twitter.com/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions).

There are other methods that `SearchClient` has and it is suggested to look through the [code](./search_client/client.py).
Documentation using `mkdocs` is currently being set up.

# TODO
- explore possible designs of a DSL for querying tweets
- higher level interface that doesn't require users to know about Twitter API
- examples
- separate clients for count, tweet lookup, and user lookup endpoint
- model for Tweet objects (currently uses dictionaries)
- documentation
- tests
- CI/CD
