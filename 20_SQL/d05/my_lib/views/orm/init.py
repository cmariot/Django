from d05.my_lib.utils import get_nav_links, get_title
from django.shortcuts import render


def init(request, exercise, previous, next="/ex02/display"):
    context = {
        "title": get_title(exercise),
        "content": [
            f"The table {exercise}_movies has been created during the migration."
        ],
        "nav_links": get_nav_links(exercise),
        "exercise": f"{exercise}",
        "previous": previous,
        "next": next,
        "active": "init",
        "created_column": True if exercise == "ex07" else False,
    }
    return render(request, "d05/templates/init.html", context)
