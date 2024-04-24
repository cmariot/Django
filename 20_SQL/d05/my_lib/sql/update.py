def update_line(cursor, table_name, title, new_opening_crawl):
    cursor.execute(
        f"""
        UPDATE {table_name} movies
        SET opening_crawl = %s
        WHERE movies.title = %s;
        """,
        (new_opening_crawl, title)
    )
