import psycopg2
from django.shortcuts import render

from d05.my_lib.utils import get_title, get_nav_links
from d05.my_lib.sql.connection import connect, close_connection
from d05.my_lib.sql.create_table import create_table
from d05.my_lib.sql.table_exists import table_exists


def init_planets(request):

    try:
        connection: psycopg2.extensions.connection = connect()
        cursor: psycopg2.extensions.cursor = connection.cursor()

        databases = {
            "ex08_planets": [
                "id SERIAL PRIMARY KEY",
                "name VARCHAR(64) UNIQUE NOT NULL",
                "climate VARCHAR",
                "diameter INT",
                "orbital_period INT",
                "population BIGINT",
                "rotation_period INT",
                "surface_water FLOAT",
                "terrain VARCHAR(128)"
            ],
            "ex08_people": [
                "id SERIAL PRIMARY KEY",
                "name VARCHAR(64) UNIQUE NOT NULL",
                "birth_year VARCHAR(32)",
                "gender VARCHAR(32)",
                "eye_color VARCHAR(32)",
                "hair_color VARCHAR(32)",
                "height INT",
                "mass FLOAT",
                "homeworld VARCHAR(64)",
                "FOREIGN KEY (homeworld) REFERENCES ex08_planets(name)"
            ]
        }

        content = []
        for table_name, columns in databases.items():
            if not table_exists(cursor, table_name):
                create_table(cursor, table_name, columns)
                connection.commit()
                content.append("OK")
            else:
                content.append(f"Table {table_name} already exists")

    except psycopg2.Error as e:
        content.append(str(e))

    finally:
        close_connection(cursor, connection)

    context = {
        "title": get_title("ex08"),
        "content": content,
        "nav_links": get_nav_links("ex08"),
        "exercise": "ex08",
        "previous": "/ex07/display",
        "next": "/ex09/display",
        "active": "init",
    }

    return render(request, "d05/templates/init.html", context)


def populate_planets(request):

    try:

        db_csv = {
            "ex08_planets": {
                "csv_file": "d05/datasets/planets.csv",
                "columns": [
                    "name",
                    "climate",
                    "diameter",
                    "orbital_period",
                    "population",
                    "rotation_period",
                    "surface_water",
                    "terrain"
                ]
            },
            "ex08_people": {
                "csv_file": "d05/datasets/people.csv",
                "columns": [
                    "name",
                    "birth_year",
                    "gender",
                    "eye_color",
                    "hair_color",
                    "height",
                    "mass",
                    "homeworld"
                ]
            }
        }

        content = []
        for table_name, table_dict in db_csv.items():
            connection: psycopg2.extensions.connection = connect()
            cursor: psycopg2.extensions.cursor = connection.cursor()
            if not table_exists(cursor, table_name):
                content.append(f"Table {table_name} does not exist")
            else:
                with open(table_dict["csv_file"], "r") as csv_content:
                    try:
                        cursor.copy_from(
                            csv_content,
                            table_name,
                            columns=table_dict["columns"],
                            null="NULL",
                        )
                        connection.commit()
                        content.append(f"{table_name}: OK")
                    except psycopg2.Error as e:
                        content.append(f"{table_name}: {e}")
                        connection.rollback()
            close_connection(cursor, connection)
    except psycopg2.Error as e:
        content.append(str(e))

    context = {
        "title": get_title("ex08"),
        "content": content,
        "nav_links": get_nav_links("ex08"),
        "exercise": "ex08",
        "previous": "/ex07/display",
        "next": "/ex09/display",
        "active": "populate",
    }

    return render(request, "d05/templates/populate.html", context)


def display_planets(request):

    data = None
    try:
        connection: psycopg2.extensions.connection = connect()
        cursor: psycopg2.extensions.cursor = connection.cursor()
        if not table_exists(cursor, "ex08_planets"):
            content = "Table does not exist"
            fields = None
            data = None
        else:
            fields = ["name", "origin", "climate"]
            cursor.execute(
                """
                SELECT people.name, planets.name, planets.climate
                FROM ex08_people people
                JOIN ex08_planets planets
                ON people.homeworld = planets.name
                WHERE planets.climate LIKE '%windy%'
                ORDER BY people.name ASC;
                """
            )
            data = cursor.fetchall()

            if not data:
                content = "No data available"
            else:
                content = None
    except psycopg2.Error as e:
        content = "Error: " + str(e)
    finally:
        close_connection(cursor, connection)

    context = {
        "title": get_title("ex08"),
        "fields": fields,
        "data": data,
        "content": content,
        "nav_links": get_nav_links("ex08"),
        "exercise": "ex08",
        "previous": "/ex07/display",
        "next": "/ex09/display",
        "active": "display",
    }
    return render(request, "d05/templates/display.html", context)
