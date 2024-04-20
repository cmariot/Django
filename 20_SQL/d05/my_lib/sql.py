import psycopg2
from django.conf import settings
from django.shortcuts import render
from ex04.forms import RemoveMovie
from ex06.forms import UpdateMovie
from django.http import HttpResponseRedirect


def get_nav_links(exercise="ex00"):
    if exercise == "ex00":
        return {
            "init": f"/{exercise}/init",
        }
    elif exercise == "ex02":
        return {
            "init": f"/{exercise}/init",
            "populate": f"/{exercise}/populate",
            "display": f"/{exercise}/display",
        }
    elif exercise == "ex03":
        return {
            "populate": f"/{exercise}/populate",
            "display": f"/{exercise}/display",
        }
    elif exercise == "ex04":
        return {
            "init": f"/{exercise}/init",
            "populate": f"/{exercise}/populate",
            "display": f"/{exercise}/display",
            "remove": f"/{exercise}/remove",
        }
    elif exercise == "ex05":
        return {
            "populate": f"/{exercise}/populate",
            "display": f"/{exercise}/display",
            "remove": f"/{exercise}/remove",
        }
    elif exercise == "ex06":
        return {
            "init": f"/{exercise}/init",
            "populate": f"/{exercise}/populate",
            "display": f"/{exercise}/display",
            "remove": f"/{exercise}/remove",
            "update": f"/{exercise}/update",
        }
    elif exercise == "ex07":
        return {
            "populate": f"/{exercise}/populate",
            "display": f"/{exercise}/display",
            "remove": f"/{exercise}/remove",
            "update": f"/{exercise}/update",
        }


def init(request, exercise="ex00", previous=None, next=None):

    """
    Initialize the database for the exercise
    """

    try:
        connection: psycopg2.extensions.connection = connect()
        cursor: psycopg2.extensions.cursor = connection.cursor()
        if not table_exists(cursor, f"{exercise}_movies"):
            if exercise == "ex06":
                create_table(cursor, f"{exercise}_movies", columns=[
                    "episode_nb    SERIAL PRIMARY KEY",
                    "title         VARCHAR(64) UNIQUE NOT NULL",
                    "opening_crawl TEXT",
                    "director      VARCHAR(32) NOT NULL",
                    "producer      VARCHAR(128) NOT NULL",
                    "release_date  DATE NOT NULL",
                    "created       TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
                    "updated       TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
                ])
            else:
                create_table(cursor, f"{exercise}_movies")
            connection.commit()
            content = "OK"
        else:
            content = "Table already exists"
    except psycopg2.Error as e:
        content = str(e)
    finally:
        close_connection(cursor, connection)

    context = {
        "title": f"{exercise}: Initialization of {exercise}_movies",
        "content": content,
        "nav_links": get_nav_links(exercise),
        "exercise": f"{exercise}",
        "previous": previous,
        "next": next,
        "active": "init",
    }

    return render(request, "d05/templates/init.html", context)


def connect(
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
) -> tuple:

    """
    Connect to a PostgreSQL database and return the connection object

    The connection parameters are read from the Django settings.

    :param user: the database user
    :param password: the database user's password
    :param host: the database host
    :param port: the database port
    :param database: the database name

    :return: the connection object
    """
    connection = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database,
    )

    return connection


def table_exists(
    cursor: psycopg2.extensions.cursor,
    table_name="ex00_movies"
) -> bool:

    """
    Check if the table referenced by 'table_name' exists in the database.
    Return a boolean.
    """

    cursor.execute(
        f"""
        SELECT * FROM information_schema.tables WHERE table_name='{table_name}'
        """
    )
    result = cursor.fetchone()
    return True if result else False


def create_table(
    cursor: psycopg2.extensions.cursor,
    table_name: str = "ex00_movies",
    columns: list = [
        "episode_nb     INTEGER PRIMARY KEY",
        "title          VARCHAR(64) UNIQUE NOT NULL",
        "opening_crawl  TEXT",
        "director       VARCHAR(32) NOT NULL",
        "producer       VARCHAR(128) NOT NULL",
        "release_date   DATE NOT NULL"
    ]
):

    cursor.execute(
        f"CREATE TABLE {table_name} ({', '.join(columns)})"
    )

    for column in columns:
        if "updated" in column or "created" in column:
            # Add a trigger to update the 'updated' column
            cursor.execute(
                """
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
                """)
            return


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

        errors = []
        title = None
        for dict in to_insert:

            try:
                title = dict.get("title")
                cursor.execute(
                    f"""
                    INSERT INTO {exercise}_movies (
                        episode_nb,
                        title,
                        director,
                        producer,
                        release_date
                    ) VALUES (
                        {dict.get("episode_nb")},
                        '{dict.get("title")}',
                        '{dict.get("director")}',
                        '{dict.get("producer")}',
                        '{dict.get("release_date")}'
                    );
                    """
                )
                connection.commit()
            except psycopg2.Error as e:
                if title:
                    errors.append(f"Error inserting {title}: {e}")
                else:
                    errors.append(str(e))
                connection.rollback()

        if not errors:
            content = "OK"
        else:
            content = "Errors occurred"

    except psycopg2.Error as e:
        content = str(e)
    finally:
        close_connection(cursor, connection)

    context = {
        "title": f"{exercise}: Populate {exercise}_movies",
        "content": content,
        "errors": errors,
        "nav_links": get_nav_links(exercise),
        "exercise": f"{exercise}",
        "previous": previous,
        "next": next,
        "active": "populate",
    }
    return render(request, "d05/templates/populate.html", context)


def insert(
    cursor: psycopg2.extensions.cursor,
    data: list,
    table_name="ex02_movies",
):
    try:
        title = None
        for dict in data:
            title = dict.get("title")
            keys = ", ".join(dict.keys())
            values = tuple(dict.values())
            values_s = ", ".join(["%s"] * len(dict))  # %s, %s, %s ...
            cursor.execute(
                f"INSERT INTO {table_name} ({keys}) VALUES ({values_s})",
                values
            )
    except psycopg2.Error as e:
        raise psycopg2.Error(f"Error inserting {title}: {e}")


def close_connection(cursor, connection):
    cursor.close()
    connection.close()


def select_columns(cursor, table_name="ex02_movies"):
    """
    Return a list with the column names of the table
    """
    cursor.execute(
        f"""
        SELECT column_name FROM information_schema.columns
        WHERE table_name = '{table_name}'
        """
    )
    return [column[0] for column in cursor.fetchall()]


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
            close_connection(cursor, connection)
            if not data:
                content = "No data available"
            else:
                content = None
    except psycopg2.Error as e:
        content = "Error: " + str(e)
    finally:
        close_connection(cursor, connection)

    context = {
        "title": f"{exercise}: Display {exercise}_movies",
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


def select(cursor, table_name="ex02_movies", fields=None):
    if fields:
        cursor.execute(
            f"""
            SELECT {fields} FROM {table_name}
            ORDER BY {table_name}.episode_nb ASC
            """
        )
    else:
        cursor.execute(
            f"SELECT * FROM {table_name} ORDER BY {table_name}.episode_nb ASC"
        )
    return cursor.fetchall()


def select_column(cursor, table_name="ex04_movies", column="title"):
    cursor.execute(
        f"SELECT {column} FROM {table_name} ORDER BY {table_name}.episode_nb ASC"
    )
    return cursor.fetchall()


def remove(request, exercise="ex04", previous=None, next=None):

    my_form = None

    if request.method == "GET":

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
            "title": f"{exercise}: Remove from {exercise}_movies",
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

        to_remove = request.POST.get("title")

        if not to_remove:
            return HttpResponseRedirect(f"/{exercise}/remove")

        try:
            connection: psycopg2.extensions.connection = connect()
            cursor: psycopg2.extensions.cursor = connection.cursor()
            if not table_exists(cursor, f"{exercise}_movies"):
                return HttpResponseRedirect(f"/{exercise}/remove")
            cursor.execute(
                f"""
                DELETE FROM {exercise}_movies movies
                WHERE movies.title = '{to_remove}';
                """
            )
            connection.commit()
        except psycopg2.Error:
            pass
        finally:
            close_connection(cursor, connection)
        return HttpResponseRedirect(f"/{exercise}/remove")


def update(request, exercise="ex04", previous=None, next=None):

    if request.method == "GET":

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
            "title": f"{exercise}: Update {exercise}_movies",
            "content": content,
            "form": my_form,
            "nav_links": get_nav_links(exercise),
            "exercise": f"{exercise}",
            "previous": previous,
            "next": next,
            "active": "update",
        }

        return render(request, "d05/templates/update.html", context)

    elif request.method == "POST":

        new_opening_crawl = request.POST.get("new_opening_crawl")
        title = request.POST.get("title")

        if not new_opening_crawl or not title:
            return HttpResponseRedirect(f"/{exercise}/update")

        try:

            connection: psycopg2.extensions.connection = connect()
            cursor: psycopg2.extensions.cursor = connection.cursor()
            if not table_exists(cursor, f"{exercise}_movies"):
                return HttpResponseRedirect(f"/{exercise}/update")
            cursor.execute(
                f"""
                UPDATE {exercise}_movies movies
                SET opening_crawl = '{new_opening_crawl}'
                WHERE movies.title = '{title}';
                """
            )
            connection.commit()
        except psycopg2.Error:
            pass
        finally:
            close_connection(cursor, connection)
        return HttpResponseRedirect(f"/{exercise}/update")
