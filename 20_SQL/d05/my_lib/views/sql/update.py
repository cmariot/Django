import psycopg2
from django.shortcuts import render
from ex06.forms import UpdateMovie
from django.http import HttpResponseRedirect

from d05.my_lib.utils import get_title, get_nav_links
from d05.my_lib.sql.connection import connect, close_connection
from d05.my_lib.sql.table_exists import table_exists
from d05.my_lib.sql.update import update_line
from d05.my_lib.sql.select import select
from d05.my_lib.sql.delete import value_not_in_table


def update(request, exercise="ex04", previous=None, next=None):

    if request.method == "GET":

        # The get method is used to display the form to update a movie
        # If the table does not exists or if there is no data, the form is not
        # displayed

        content, my_form = None, None

        try:

            connection: psycopg2.extensions.connection = connect()
            cursor: psycopg2.extensions.cursor = connection.cursor()

            if not table_exists(cursor, f"{exercise}_movies"):
                content = "Table does not exist"
            else:
                data = select(cursor, f"{exercise}_movies")
                if not data:
                    content = "No data available"
                else:
                    titles = []
                    for movie in data:
                        titles.append(movie[1])
                    my_form = UpdateMovie(
                        choices=[(title, title) for title in titles]
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
            "exercise": exercise,
            "previous": previous,
            "next": next,
            "active": "update",
        }
        return render(request, "d05/templates/update.html", context)

    elif request.method == "POST":

        # The post method is used to update the opening crawl of a movie
        # in the database

        new_opening_crawl = request.POST.get("new_opening_crawl")
        title = request.POST.get("title")

        if not new_opening_crawl or not title:
            return HttpResponseRedirect(f"/{exercise}/update")

        try:

            connection: psycopg2.extensions.connection = connect()
            cursor: psycopg2.extensions.cursor = connection.cursor()

            if table_exists(cursor, f"{exercise}_movies"):
                if not value_not_in_table(
                    cursor, f"{exercise}_movies", "title", title
                ):
                    update_line(
                        cursor, f"{exercise}_movies", title, new_opening_crawl
                    )
                    connection.commit()

        except psycopg2.Error:
            pass

        finally:
            close_connection(cursor, connection)

        return HttpResponseRedirect(f"/{exercise}/update")
