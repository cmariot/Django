from d05.my_lib.utils import get_nav_links, get_title
from django.shortcuts import render


def display(request, Movies, exercise="ex00", previous=None, next=None):

    content, data, fields = None, None, None

    if not Movies.objects.exists():
        content = "The table does not exists"
    else:
        fields = Movies._meta.get_fields()
        data = Movies.objects.all().order_by("episode_nb")
        if len(data) == 0:
            content = "The table is empty"

    context = {
        "title": get_title(exercise),
        "content": content,
        "fields": fields,
        "data": data,
        "nav_links": get_nav_links(exercise),
        "previous": previous,
        "next": next,
        "active": "display",
        "created_column": True if exercise == "ex07" else False,
    }
    return render(request, "d05/templates/display_model.html", context)
