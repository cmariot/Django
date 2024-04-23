from django.shortcuts import render
from .models import People
from d05.my_lib.sql import get_nav_links, get_title


def display(request):

    data = People.objects.filter(
        homeworld__climate__icontains="windy"
    ).order_by("name")

    fields = ["name", "origin", "climate"]

    print(data)

    context = {
        'title': get_title("ex09"),
        'data': data,
        'fields': fields,
        'nav_links': get_nav_links("ex09"),
        'previous': '/ex08/display',
        'active': 'display'
    }
    return render(request, 'd05/templates/display_people.html', context)
