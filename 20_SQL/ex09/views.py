from django.shortcuts import render
from .models import People
from d05.my_lib.views.sql.planets import get_nav_links, get_title


def display(request):

    data = People.objects.filter(
        homeworld__climate__contains="windy"
    ).order_by("name")

    fields = ["name", "origin", "climate"]

    context = {
        'title': get_title("ex09"),
        'data': data,
        'fields': fields,
        'nav_links': get_nav_links("ex09"),
        'previous': '/ex08/display',
        'next': '/ex10',
        'active': 'display'
    }
    return render(request, 'd05/templates/display_people.html', context)
