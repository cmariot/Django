from django.shortcuts import render
from django.http import HttpResponse
import psycopg2


def init(request):

    def connect():
        return psycopg2.connect(
            user="djangouser",
            password="secret",
            host="localhost",
            port="5432",
            database="formationdjango",
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
            return HttpResponse("Table already exists")
        else:
            create_table(cursor)
            close_connection(cursor, connection)
            return HttpResponse("OK")
    except psycopg2.Error as e:
        close_connection(cursor, connection)
        return HttpResponse(e)
