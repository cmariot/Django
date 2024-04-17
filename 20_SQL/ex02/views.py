from django.shortcuts import render
from django.http import HttpResponse
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

    def table_exists(cursor, table_name="ex02_movies"):
        cursor.execute(
            "SELECT * FROM information_schema.tables " +
            f"WHERE table_name='{table_name}'"
        )
        return cursor.fetchone()

    def create_table(cursor):
        cursor.execute(
            "CREATE TABLE ex02_movies ("
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
        context = {
            "content": content
        }
        return render(request, "ex02/templates/init.html", context)
    except psycopg2.Error as e:
        close_connection(cursor, connection)
        return HttpResponse(e)


def populate(request):

    to_insert = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19"
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16"
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19"
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25"
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kutz, Rick McCallum",
            "release_date": "1980-05-17"
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25"
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J.J. Abrams",
            "producer": "Kathleen Kennedy, J.J. Abrams, Bryan Burk",
            "release_date": "2015-12-11"
        }
    ]

    def connect():
        return psycopg2.connect(
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
        )

    def insert(cursor, data):
        try:
            title = None
            for row in data:
                title = row.get("title")
                cursor.execute(
                    "INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (row["episode_nb"], row["title"], row["director"], row["producer"], row["release_date"])
                )
        except psycopg2.Error as e:
            raise psycopg2.Error(f"Error inserting {title}: {e}")

    def close_connection(cursor, connection):
        cursor.close()
        connection.close()

    try:
        connection = connect()
        cursor = connection.cursor()
        insert(cursor, to_insert)
        connection.commit()
        close_connection(cursor, connection)
        content = "OK"
    except psycopg2.Error as e:
        close_connection(cursor, connection)
        content = e
    context = {
        "content": content
    }
    return render(request, "ex02/templates/populate.html", context)


def display(request):

    def connect():
        return psycopg2.connect(
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
        )

    def select(cursor):
        cursor.execute("SELECT * FROM ex02_movies")
        return cursor.fetchall()

    def close_connection(cursor, connection):
        cursor.close()
        connection.close()

    try:
        connection = connect()
        cursor = connection.cursor()
        data = select(cursor)
        close_connection(cursor, connection)
        if not data:
            return HttpResponse("No data available")
        context = {
            "data": data,
            "nav_links": {
                "Initialisation": "/ex02/init",
                "Peuplement": "/ex02/populate",
                "Affichage": "/ex02/display",
            },
        }
        return render(request, "ex02/templates/display.html", context)
    except psycopg2.Error as e:
        close_connection(cursor, connection)
        return HttpResponse(e)
