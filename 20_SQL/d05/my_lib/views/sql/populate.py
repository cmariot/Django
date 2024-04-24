import psycopg2
from django.shortcuts import render

from d05.my_lib.utils import get_title, get_nav_links
from d05.my_lib.sql.connection import connect, close_connection
from d05.my_lib.sql.insert import insert


def populate(request, exercise="ex00", previous=None, next=None):

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

        connection: psycopg2.extensions.connection = connect()
        cursor: psycopg2.extensions.cursor = connection.cursor()

        content = []
        title = None

        for dict in to_insert:

            try:

                title = dict.get("title")
                insert(cursor, dict, f"{exercise}_movies")
                connection.commit()
                content.append(f"{title}: OK")

            except psycopg2.Error as e:

                if title:
                    content.append(f"{title}: {e}")
                else:
                    content.append(str(e))

                connection.rollback()

    except Exception as e:
        content.append(str(e))

    finally:
        close_connection(cursor, connection)

    context = {
        "title": get_title(exercise),
        "content": content,
        "nav_links": get_nav_links(exercise),
        "exercise": f"{exercise}",
        "previous": previous,
        "next": next,
        "active": "populate",
    }
    return render(request, "d05/templates/populate.html", context)
