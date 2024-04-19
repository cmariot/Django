from ex03.models import Movies
from d05.my_lib.sql import get_nav_links
from django.shortcuts import render
from ex04.forms import MyForm
from django.http import HttpResponseRedirect


def populate(request, exercise="ex00", previous=None, next=None):

    to_insert = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19"
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16"
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19"
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25"
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kutz, Rick McCallum",
            "release_date": "1980-05-17"
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25"
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J.J. Abrams",
            "producer": "Kathleen Kennedy, J.J. Abrams, Bryan Burk",
            "release_date": "2015-12-11"
        }
    ]

    errors = []
    title = None
    for dict in to_insert:
        try:
            title = dict.get("title")
            Movies.objects.create(
                episode_nb=dict["episode_nb"],
                title=dict["title"],
                director=dict["director"],
                producer=dict["producer"],
                release_date=dict["release_date"]
            )
        except Exception as e:
            if title:
                errors.append(f"Error inserting {title}: {e}")
            else:
                errors.append(str(e))

    if not errors:
        content = "OK"
    else:
        content = "Errors occurred"

    context = {
        "title": f"{exercise}: Populate {exercise}_movies",
        "content": content,
        "errors": errors,
        "nav_links": get_nav_links(exercise),
        "exercise": f"{exercise}",
        "previous": previous,
        "next": next,
        "active": "populate",
    }
    return render(request, "d05/templates/populate.html", context)


def display(request, exercise="ex00", previous=None, next=None):

    content, data = None, None

    if not Movies.objects.exists():
        content = "The table does not exists"
    else:
        data = Movies.objects.all()
        if len(data) == 0:
            content = "The table is empty"

    context = {
        "content": content,
        "data": data,
        "nav_links": get_nav_links(exercise),
        "previous": previous,
        "next": next,
        "active": "display",
    }
    return render(request, "d05/templates/display_model.html", context)


def remove(request, exercise="ex05", previous=None, next=None):

    my_form = None

    if request.method == "GET":

        if not Movies.objects.exists():
            content = "The table does not exists"
        else:
            data = Movies.objects.all()
            if not data:
                content = "No data available"
            else:
                titles = []
                for movie in data:
                    titles.append(movie.title)
                my_form = MyForm(
                    choices=[(title, title) for title in titles]
                )
                content = None

        context = {
            "title": f"{exercise}: Remove from {exercise}_movies",
            "content": content,
            "form": my_form,
            "nav_links": get_nav_links(exercise),
            "exercise": f"{exercise}",
            "previous": previous,
            "next": next,
            "active": "remove",
        }

        return render(request, "d05/templates/remove.html", context)

    elif request.method == "POST":

        to_remove = request.POST.get("title")

        if not to_remove:
            return HttpResponseRedirect("/ex05/remove")

        if not Movies.objects.exists():
            return HttpResponseRedirect("/ex05/remove")

        Movies.objects.filter(title=to_remove).delete()

        return HttpResponseRedirect("/ex05/remove")

