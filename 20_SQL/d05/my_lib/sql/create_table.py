import psycopg2


def create_table(
    cursor: psycopg2.extensions.cursor,
    table_name: str,
    columns: list,
    trigger: str = None
):

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)});"
    )

    if trigger:
        cursor.execute(trigger)
