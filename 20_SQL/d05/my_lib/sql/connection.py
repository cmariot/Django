from django.conf import settings
import psycopg2


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


def close_connection(cursor, connection):
    cursor.close()
    connection.close()
