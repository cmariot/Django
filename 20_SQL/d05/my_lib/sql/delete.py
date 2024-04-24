
def value_not_in_table(cursor, table_name, column_name, value):
    """
    Return True if the value is not in the table, False otherwise.
    """

    cursor.execute(
        f"SELECT {column_name} FROM {table_name} WHERE {column_name} = %s;",
        (value,)
    )

    return not cursor.fetchone()


def remove_line(cursor, table_name, column_name, value):
    cursor.execute(
        f"DELETE FROM {table_name} WHERE {column_name} = %s;",
        (value,)
    )
