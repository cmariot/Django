import psycopg2
from django.shortcuts import render

from d05.my_lib.utils import get_title, get_nav_links
from d05.my_lib.sql.connection import connect, close_connection
from d05.my_lib.sql.table_exists import table_exists
from d05.my_lib.sql.select import select, select_columns


def display(request, exercise="ex00", previous=None, next=None):

    try:

        connection: psycopg2.extensions.connection = connect()
        cursor: psycopg2.extensions.cursor = connection.cursor()

        if not table_exists(cursor, f"{exercise}_movies"):
            content = "Table does not exist"
            fields = None
            data = None

        else:
            fields = select_columns(cursor, f"{exercise}_movies")
            data = select(cursor, f"{exercise}_movies", fields=", ".join(fields))
            content = "No data available" if not data else None

    except psycopg2.Error as e:
        content = "Error: " + str(e)

    finally:
        close_connection(cursor, connection)

    context = {
        "title": get_title(exercise),
        "fields": fields,
        "data": data,
        "content": content,
        "nav_links": get_nav_links(exercise),
        "exercise": f"{exercise}",
        "previous": previous,
        "next": next,
        "active": "display",
    }
    return render(request, "d05/templates/display.html", context)
