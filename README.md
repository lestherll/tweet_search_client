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
tweets = client.get_tweet(query=["from:twitterDev"])    
```

# Usage
[SearchClient](search_client/client.py) will be the interface exposed for 
the user. It will contain everything to do with searching tweets. 
Currently, the library is minimal and incomplete:
- you can only currently fetch basic info from tweets although `SearchClient.get_tweet`
allows you to build primitive queries that are not too far off from how Twitter API
wants you to build queries 
- You can get tweets from a certain author.

# TODO
- ~~A richer and higher level way to mine tweets (include parameters that API allows)~~
  - explore possible designs of a DSL for querying
- examples
