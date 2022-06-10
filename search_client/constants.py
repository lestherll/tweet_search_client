from dataclasses import dataclass

from dotenv import dotenv_values


@dataclass(frozen=True)
class Config:
    BASE_URL: str
    BEARER_TOKEN: str | None = None


config = Config(
    BASE_URL="https://api.twitter.com/2",
    **dotenv_values("./.env"),
)
