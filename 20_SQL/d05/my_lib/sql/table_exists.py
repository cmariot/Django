import psycopg2


def table_exists(
    cursor: psycopg2.extensions.cursor,
    table_name="ex00_movies"
) -> bool:

    """
    Check if the table referenced by 'table_name' exists in the database.
    Return a boolean.
    """

    cursor.execute(
        "SELECT * FROM information_schema.tables WHERE table_name=%s",
        (table_name,)
    )
    result = cursor.fetchone()
    return True if result else False
