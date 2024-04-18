from django.shortcuts import render
import psycopg2
from d05.my_lib.sql import (
    connect, close_connection, table_exists, create_table
)


def init(request):
    try:
        connection, cursor = connect()
        if table_exists(cursor):
            content = "Table already exists"
        else:
            create_table(cursor, connection)
            content = "OK"
        close_connection(cursor, connection)
    except psycopg2.Error as e:
        content = "Error:" + e
        close_connection(cursor, connection)
    context = {
        "title": "Initialisation",
        "content": content
    }
    return render(request, "ex00/templates/init.html", context)
