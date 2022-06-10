# Twitter Search Client (WIP)

An unofficial **WIP** client for the twitter API that has only one goal; search for tweets.


# Setup

Project requires you to create a `.env` file at the project root.
The library forces you to create one by default so that there is 
less risk in leaking your credentials accidentally.

`.env` file should look like below
```
BEARER_TOKEN=your_bearer_token_that_you_got_from_twitter
```

# Usage
[SearchClient](bulan/client.py) will be the interface exposed for 
the user. It will contain everything to do with searching tweets. 
Currently, the library is minimal and incomplete:
- you can only currently fetch basic info from tweets although `SearchClient.get_tweet`
allows you to build primitive queries that are not too far off from how Twitter API
wants you to build queries 
- You can get tweets from a certain author.

# TODO
- A richer and higher level way to mine tweets (include parameters that API allows)
- examples