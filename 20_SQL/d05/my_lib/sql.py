import psycopg2
from django.conf import settings


def connect(
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
) -> tuple:

    """
    Connect to a PostgreSQL database and return the connection and a cursor.

    The connection parameters are read from the Django settings.

    :param user: the database user
    :param password: the database user's password
    :param host: the database host
    :param port: the database port
    :param database: the database name

    :return: the connection and the cursor objects
    """
    connection = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database,
    )

    cursor = connection.cursor()

    return connection, cursor


def table_exists(
    cursor: psycopg2.extensions.cursor,
    table_name="ex00_movies"
) -> bool:

    """
    Check if the table referenced by 'table_name' exists in the database.
    Return a boolean.
    """

    cursor.execute(
        f"""
        SELECT * FROM information_schema.tables
        WHERE table_name='{table_name}'
        """
    )
    result = cursor.fetchone()
    return True if result else False


def create_table(
    cursor: psycopg2.extensions.cursor,
    connection: psycopg2.extensions.connection,
    table_name: str = "ex00_movies",
    columns: list = [
        "episode_nb     INTEGER PRIMARY KEY",
        "title          VARCHAR(64) UNIQUE NOT NULL",
        "opening_crawl  TEXT",
        "director       VARCHAR(32) NOT NULL",
        "producer       VARCHAR(128) NOT NULL",
        "release_date   DATE NOT NULL"
    ]
):
    cursor.execute(
        f"CREATE TABLE {table_name} ({', '.join(columns)})"
    )
    connection.commit()


def insert(
    cursor: psycopg2.extensions.cursor,
    data: list,
    table_name="ex02_movies",
):
    try:
        title = None
        for dict in data:
            title = dict.get("title")
            keys = ", ".join(dict.keys())
            values = tuple(dict.values())
            values_s = ", ".join(["%s"] * len(dict))
            cursor.execute(
                f"INSERT INTO {table_name} ({keys}) VALUES ({values_s})",
                values
            )
    except psycopg2.Error as e:
        raise psycopg2.Error(f"Error inserting {title}: {e}")


def close_connection(cursor, connection):
    cursor.close()
    connection.close()


def select(cursor, table_name="ex02_movies"):
    cursor.execute(
        f"SELECT * FROM {table_name}"
    )
    return cursor.fetchall()
