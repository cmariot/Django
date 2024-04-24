import psycopg2


def insert(
    cursor: psycopg2.extensions.cursor,
    dict: dict,
    table_name="ex02_movies",
):
    keys = ", ".join(dict.keys())
    values_s = ", ".join(["%s"] * len(dict))  # %s, %s, %s ...
    values = tuple(dict.values())
    cursor.execute(
        f"INSERT INTO {table_name} ({keys}) VALUES ({values_s})",
        values
    )
