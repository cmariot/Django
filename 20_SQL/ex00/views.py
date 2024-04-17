from django.shortcuts import render
import psycopg2
from django.conf import settings


def init(request):

    def connect():
        return psycopg2.connect(
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
        )

    def table_exists(cursor, table_name="ex00_movies"):
        cursor.execute(
            "SELECT * FROM information_schema.tables " +
            f"WHERE table_name='{table_name}'"
        )
        return cursor.fetchone()

    def create_table(cursor):
        cursor.execute(
            "CREATE TABLE ex00_movies ("
            "title VARCHAR(64) NOT NULL, "
            "episode_nb SERIAL PRIMARY KEY, "
            "opening_crawl TEXT, "
            "director VARCHAR(32) NOT NULL, "
            "producer VARCHAR(128) NOT NULL, "
            "release_date DATE NOT NULL"
            ")"
        )
        connection.commit()

    def close_connection(cursor, connection):
        cursor.close()
        connection.close()

    try:
        connection = connect()
        cursor = connection.cursor()
        if table_exists(cursor):
            close_connection(cursor, connection)
            content = "Table already exists"
        else:
            create_table(cursor)
            close_connection(cursor, connection)
            content = "OK"
    except psycopg2.Error as e:
        close_connection(cursor, connection)
        content = e
    context = {
        "title": "Initialisation",
        "content": content
    }
    return render(request, "ex00/templates/init.html", context)
