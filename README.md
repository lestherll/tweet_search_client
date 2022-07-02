# Twitter Search Client (WIP)
An unofficial **WIP** client for the twitter API that has only one goal; search for tweets.


# Installation
Package is not ready for PyPI yet but it can be installed directly from GitHub using `pip`.
```shell
pip install git+https://github.com/lestherll/twitter_search_client
```

# Setup and Prerequisites
Before everything, make sure that you have a developer account and a bearer token 
from Twitter. You can find out how to get one [here](https://developer.twitter.com/en/docs/twitter-api)

Project requires you to create a `.env` file at the project root.
The library forces you to create one by default so that there is 
less risk in leaking your credentials accidentally.

`.env` file should look like below
```env
BEARER_TOKEN=your_bearer_token_that_you_got_from_twitter
```

In environments where creating is not possible, you can just pass
the bearer token directly to the `SearchClient` class. You must, however,
be aware that you would be exposing your keys to others.
```py
from search_client import SearchClient

client = SearchClient("your_keys_must_be_string")

# do work with client
tweets = client.get_recent_tweets(query=["from:twitterDev"])
```

# Usage
[SearchClient](search_client/client.py) will be the interface exposed to 
the user. It will contain everything to do with searching tweets. It is 
planned to use other endpoints of the Twitter API and expose them through
other client types.

### Main endpoints supported
| Twitter API Endpoint  | Method                           | V2 Access Levels |
|-----------------------|----------------------------------|------------------|
| `/search/recent`      | `SearchClient.get_recent_tweets` | Developer        |
| `/search/all`         | `SearchClient.get_all_tweets`    | Academic         |
| `/tweets/counts/all`  | `SearchClient.get_tweet_counts`  | Academic         |

These methods are low-level wrappers over raw requests to their respective 
endpoints. [Enumerations](./search_client/field_enums.py) are provided for
convenience of passing [fields](https://developer.twitter.com/en/docs/twitter-api/fields)
and [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions).

There are other methods that `SearchClient` has and it is suggested to look
thorugh the [code](./search_client/client.py).

# TODO
- explore possible designs of a DSL for querying tweets
- higher level interface that doesn't require users to know about Twitter API
- examples
- separate clients for count, tweet lookup, and user lookup endpoint
- model for Tweet objects (currently uses dictionaries)
