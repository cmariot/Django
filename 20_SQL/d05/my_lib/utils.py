def get_title(exercise="ex00"):
    if exercise == "ex00":
        return "ex00: SQL Initialization of a table"
    elif exercise == "ex01":
        return "ex01: ORM Initialization of a table"
    elif exercise == "ex02":
        return "ex02: SQL Insertion of data"
    elif exercise == "ex03":
        return "ex03: ORM Insertion of data"
    elif exercise == "ex04":
        return "ex04: SQL Deletion of data"
    elif exercise == "ex05":
        return "ex05: ORM Deletion of data"
    elif exercise == "ex06":
        return "ex06: SQL Update of data"
    elif exercise == "ex07":
        return "ex07: ORM Update of data"
    elif exercise == "ex08":
        return "ex08: SQL Foreign Keys"
    elif exercise == "ex09":
        return "ex09: ORM Foreign Keys"
    elif exercise == "ex10":
        return "ex10: ORM Many-to-Many"


def get_nav_links(exercise="ex00"):
    if exercise == "ex02":
        return {
            "display": f"/{exercise}/display",
            "init": f"/{exercise}/init",
            "populate": f"/{exercise}/populate",
        }
    elif exercise == "ex03":
        return {
            "display": f"/{exercise}/display",
            "populate": f"/{exercise}/populate",
        }
    elif exercise == "ex04":
        return {
            "display": f"/{exercise}/display",
            "init": f"/{exercise}/init",
            "populate": f"/{exercise}/populate",
            "remove": f"/{exercise}/remove",
        }
    elif exercise == "ex05":
        return {
            "display": f"/{exercise}/display",
            "populate": f"/{exercise}/populate",
            "remove": f"/{exercise}/remove",
        }
    elif exercise == "ex06":
        return {
            "display": f"/{exercise}/display",
            "init": f"/{exercise}/init",
            "populate": f"/{exercise}/populate",
            "update": f"/{exercise}/update",
        }
    elif exercise == "ex07":
        return {
            "display": f"/{exercise}/display",
            "populate": f"/{exercise}/populate",
            "update": f"/{exercise}/update",
        }
    elif exercise == "ex08":
        return {
            "display": f"/{exercise}/display",
            "init": f"/{exercise}/init",
            "populate": f"/{exercise}/populate",
        }
