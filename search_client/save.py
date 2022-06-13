from __future__ import annotations

import csv
import json


def write_to_csv(tweets: list[dict[str, str]], filename: str) -> None:
    """Write tweets to csv file

    Args:
        tweets (list[dict[str, str]]): list of tweets
        filename (str): to save to
    """
    assert len(tweets) != 0, "tweets must not be empty"

    with open(filename, "w", newline="") as csvfile:
        fieldnames = tweets[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for t in tweets:
            writer.writerow(t)


def write_to_json(tweets: list[dict[str, str]], filename: str) -> None:

    with open(filename, "w") as jsonfile:
        jsonfile.write(json.dumps(tweets, indent=4))
