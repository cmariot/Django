def select(cursor, table_name="ex02_movies", fields=None):
    """
    Return all the rows of the table in the order of the episode_nb
    If fields is not None, return only the specified fields
    """
    if fields:
        return select_column(cursor, table_name, fields)
    else:
        cursor.execute(
            f"""
            SELECT * FROM {table_name}
            ORDER BY {table_name}.episode_nb ASC
            """
        )
    return cursor.fetchall()


def select_column(cursor, table_name="ex04_movies", column="title"):
    """
    Return all the values of the column in the order of the episode_nb
    """
    cursor.execute(
        f"""
        SELECT {column} FROM {table_name}
        ORDER BY {table_name}.episode_nb ASC
        """
    )
    return cursor.fetchall()


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
