"""Handy enumerations for relevant query parameters 
"""

from enum import Enum


class SortOrder(str, Enum):
    RELEVANCY = "relevancy"
    RECENCY = "recency"


class Expansions(str, Enum):
    ATTACHMENT_POLL_IDS = "attachment.poll_ids"
    ATTACHMENT_MEDIA_KEYS = "attachment.media_keys"
    AUTHOR_ID = "author_id"
    ENTITIES_MENTIONS_USERNAME = "entities.mentions.username"
    GEO_PLACE_ID = "geo.place_id"
    IN_REPLY_TO_USER_ID = "in_reply_to_user_id"
    REFERENCED_TWEETS_ID = "referenced_tweets.id"
    REFERENCED_TWEETS_ID_AUTHOR_ID = "referenced_tweets.id.author_id"


class MediaFields(str, Enum):
    DURATION_MS = "duration_ms"
    HEIGHT = "height"
    MEDIA_KEY = "media_key"
    PREVIEW_IMAGE_URL = "preview_image_url"
    TYPE = "type"
    URL = "url"
    WIDTH = "width"
    PUBLIC_METRICS = "public_metrics"
    NON_PUBLIC_METRICS = "non_public_metrics"
    ORGANIC_METRICS = "organic_metrics"
    PROMOTED_METRICS = "promoted_metrics"
    ALT_TEXT = "alt_text"


class PlaceFields(str, Enum):
    CONTAINED_WITHIN = "contained_within"
    COUNTRY = "country"
    COUNTRY_CODE = "country_code"
    FULL_NAME = "full_name"
    GEO = "geo"
    ID = "id"
    NAME = "name"
    PLACE_TYPE = "place_type"


class PollFields(str, Enum):
    DURATION_MINUTES = "duration_minutes"
    END_DATETIME = "end_datetime"
    ID = "id"
    OPTIONS = "options"
    VOTING_STATUS = "voting status"


class TweetFields(str, Enum):
    ATTACHMENTS = "attachments"
    AUTHOR_ID = "author_id"
    CONTEXT_ANNOTATIONS = "context_annotations"
    CONVERSATION_ID = "conversation_id"
    CREATED_AT = "created_at"
    ENTITIES = "entities"
    GEO = "geo"
    ID = "id"
    IN_REPLY_TO_USER_ID = "in_reply_to_user_id"
    LANG = "lang"
    PUBLIC_METRICS = "public_metrics"
    POSSIBLY_SENSITIVE = "possibly_sensitive"
    REFERENCED_TWEETS = "referenced_tweets"
    REPLY_SETTINGS = "reply_settings"
    SOURCE = "source"
    TEXT = "text"
    WITHHELD = "withheld"


# tweet_fields = [
#     "attachments",
#     "author_id",
#     "context_annotations",
#     "conversation_id",
#     "created_at",
#     "entities",
#     "geo",
#     "id",
#     "in_reply_to_user_id",
#     "lang",
#     "public_metrics",
#     "possibly_sensitive",
#     "referenced_tweets",
#     "reply_settings",
#     "source",
#     "text",
#     "withheld",
# ]

# TweetFields = Enum("TweetFields", {k.upper(): k for k in tweet_fields})


class UserFields(str, Enum):
    CREATED_AT = "created_at"
    DESCRIPTION = "description"
    ENTITIES = "entities"
    ID = "id"
    LOCATION = "location"
    NAME = "name"
    PINNED_TWEET_ID = "pinned_tweet_id"
    PROFILE_IMAGE_URL = "profile_image_url"
    PROTECTED = "protected"
    PUBLIC_METRICS = "public_metrics"
    URL = "url"
    USERNAME = "username"
    VERIFIED = "verified"
    WITHHELD = "withheld"
