import psycopg2


def create_table(
    cursor: psycopg2.extensions.cursor,
    table_name: str = "ex00_movies",
    columns: list = [
        "episode_nb     INTEGER PRIMARY KEY",
        "title          VARCHAR(64) UNIQUE NOT NULL",
        "opening_crawl  TEXT",
        "director       VARCHAR(32) NOT NULL",
        "producer       VARCHAR(128) NOT NULL",
        "release_date   DATE NOT NULL"
    ],
    trigger: str = None
):

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)});"
    )

    if trigger:
        cursor.execute(trigger)
