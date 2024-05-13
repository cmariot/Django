import psycopg2
from django.shortcuts import render

from d05.my_lib.utils import get_title, get_nav_links
from d05.my_lib.sql.connection import connect, close_connection
from d05.my_lib.sql.create_table import create_table
from d05.my_lib.sql.table_exists import table_exists


def init(request, exercise="ex00", previous=None, next=None):

    """
    Create a table in the database if it does not exist and render the
    init.html template with the result.
    """

    try:

        content = []
        connection: psycopg2.extensions.connection = connect()
        cursor: psycopg2.extensions.cursor = connection.cursor()

        if exercise != "ex06":

            create_table(cursor, f"{exercise}_movies", columns=[
                "episode_nb    INTEGER PRIMARY KEY",
                "title         VARCHAR(64) UNIQUE NOT NULL",
                "opening_crawl TEXT",
                "director      VARCHAR(32) NOT NULL",
                "producer      VARCHAR(128) NOT NULL",
                "release_date  DATE NOT NULL"
            ])

        else:

            # The ex06_movies table has two additional columns:
            # created and updated
            # The updated column is updated automatically during an update
            # due to the trigger

            create_table(
                cursor,
                f"{exercise}_movies",
                columns=[
                    "episode_nb    INTEGER PRIMARY KEY",
                    "title         VARCHAR(64) UNIQUE NOT NULL",
                    "opening_crawl TEXT",
                    "director      VARCHAR(32) NOT NULL",
                    "producer      VARCHAR(128) NOT NULL",
                    "release_date  DATE NOT NULL",
                    "created       TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
                    "updated       TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
                ],
                trigger="""
                    CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                    RETURNS TRIGGER AS $$
                    BEGIN
                    NEW.updated = now();
                    NEW.created = OLD.created;
                    RETURN NEW;
                    END;
                    $$ language 'plpgsql';
                    CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                    ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
                    update_changetimestamp_column();
                """
            )

        connection.commit()
        content.append("OK")

    except psycopg2.Error as e:
        content.append(str(e))

    finally:
        close_connection(cursor, connection)

    context = {
        "title": get_title(exercise),
        "content": content,
        "nav_links": get_nav_links(exercise),
        "exercise": exercise,
        "previous": previous,
        "next": next,
        "active": "init",
    }

    return render(request, "d05/templates/init.html", context)
