import sqlite3
from typing import final

default_conn = sqlite3.connect("tweets.db")


def save_to_db(
    tweets: list[dict],
    conn: sqlite3.Connection | str,
) -> None:

    assert len(tweets) != 0, "tweets should not be empty"

    if isinstance(conn, str):
        conn = sqlite3.connect(conn)

    cur = conn.cursor()
    cur.execute(
        """\
    create table if not exists Tweet (
        tweet_id integer primary key,
        text text not null
        );
    """
    )

    try:

        for t in tweets:
            cur.execute("INSERT INTO Tweet (tweet_id, text) values (?, ?)", (t["id"], t["text"]))
        conn.commit()
    except (sqlite3.IntegrityError, sqlite3.OperationalError) as err:
        print(err)
    finally:
        cur.close()

        if isinstance(conn, str):
            conn.close()
