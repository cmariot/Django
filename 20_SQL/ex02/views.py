from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from d05.my_lib.sql import (
    connect, table_exists, close_connection, create_table, insert, select
)


def init(request):
    try:
        connection, cursor = connect()
        if table_exists(cursor, "ex02_movies"):
            content = "Table already exists"
        else:
            create_table(cursor, connection, "ex02_movies")
            content = "OK"
        close_connection(cursor, connection)
        context = {
            "title": "Ex02: Initialization of ex02_movies",
            "nav_links": {
                "Initialisation": "/ex02/init",
                "Peuplement": "/ex02/populate",
                "Affichage": "/ex02/display",
            },
            "content": content
        }
        return render(request, "ex02/templates/init.html", context)
    except psycopg2.Error as e:
        close_connection(cursor, connection)
        context = {
            "title": "Ex02: Initialization of ex02_movies",
            "nav_links": {
                "Initialisation": "/ex02/init",
                "Peuplement": "/ex02/populate",
                "Affichage": "/ex02/display",
            },
            "content": e
        }
        return render(request, "ex02/templates/init.html", context)


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

    try:
        connection, cursor = connect()
        insert(cursor, to_insert)
        connection.commit()
        close_connection(cursor, connection)
        content = "OK"
    except psycopg2.Error as e:
        close_connection(cursor, connection)
        content = e
    context = {
        "title": "Ex02: Populate ex02_movies",
        "nav_links": {
            "Initialisation": "/ex02/init",
            "Peuplement": "/ex02/populate",
            "Affichage": "/ex02/display",
        },
        "content": content
    }
    return render(request, "ex02/templates/populate.html", context)


def display(request):

    try:
        connection, cursor = connect()
        data = select(cursor)
        close_connection(cursor, connection)
        if not data:
            content = "No data available"
        else:
            content = None
        context = {
            "data": data,
            "nav_links": {
                "Initialisation": "/ex02/init",
                "Peuplement": "/ex02/populate",
                "Affichage": "/ex02/display",
            },
            "content": content
        }
        return render(request, "ex02/templates/display.html", context)
    except psycopg2.Error as e:
        close_connection(cursor, connection)
        return HttpResponse(e)
