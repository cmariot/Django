import psycopg2
from django.shortcuts import render
from ex04.forms import RemoveMovie
from django.http import HttpResponseRedirect

from d05.my_lib.utils import get_title, get_nav_links
from d05.my_lib.sql.connection import connect, close_connection
from d05.my_lib.sql.table_exists import table_exists
from d05.my_lib.sql.select import select_column
from d05.my_lib.sql.delete import value_not_in_table, remove_line


def remove(request, exercise="ex04", previous=None, next=None):

    if request.method == "GET":

        # The get method is used to display the form to remove a movie
        # If the table does not exists or if there is no data, the form is not
        # displayed

        content, my_form = None, None

        try:

            connection: psycopg2.extensions.connection = connect()
            cursor: psycopg2.extensions.cursor = connection.cursor()

            if not table_exists(cursor, f"{exercise}_movies"):
                content = "Table does not exist"
            else:
                data = select_column(cursor, f"{exercise}_movies", "title")
                film_titles = [d[0] for d in data]
                if not film_titles:
                    content = "No data available"
                else:
                    my_form = RemoveMovie(
                        choices=[(title, title) for title in film_titles]
                    )
                    content = None

        except psycopg2.Error as e:
            content = str(e)

        finally:
            close_connection(cursor, connection)

        context = {
            "title": get_title(exercise),
            "content": content,
            "form": my_form,
            "nav_links": get_nav_links(exercise),
            "exercise": f"{exercise}",
            "previous": previous,
            "next": next,
            "active": "remove",
        }

        return render(request, "d05/templates/remove.html", context)

    elif request.method == "POST":

        # The post method is used to remove a movie from the database

        to_remove = request.POST.get("title")

        if not to_remove:
            return HttpResponseRedirect(f"/{exercise}/remove")

        try:

            connection: psycopg2.extensions.connection = connect()
            cursor: psycopg2.extensions.cursor = connection.cursor()

            # if the table exists and the movie is in the table, remove it
            if table_exists(cursor, f"{exercise}_movies"):
                if not value_not_in_table(
                    cursor, f"{exercise}_movies", "title", to_remove
                ):
                    remove_line(cursor, f"{exercise}_movies", "title", to_remove)
                    connection.commit()

        except psycopg2.Error:
            pass

        finally:
            close_connection(cursor, connection)

        return HttpResponseRedirect(f"/{exercise}/remove")
