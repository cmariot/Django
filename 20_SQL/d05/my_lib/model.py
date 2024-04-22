from d05.my_lib.sql import get_nav_links, get_title
from django.shortcuts import render
from ex04.forms import RemoveMovie
from ex06.forms import UpdateMovie
from django.http import HttpResponseRedirect


def init(request, exercise, previous, next="/ex02/display"):
    context = {
        "title": get_title(exercise),
        "content": f"The table {exercise}_movies has been " +
        "created during the migration.",
        "nav_links": get_nav_links(exercise),
        "exercise": f"{exercise}",
        "previous": previous,
        "next": next,
        "active": "init",
        "created_column": display_created_updated(request, exercise),
    }
    return render(request, "d05/templates/init.html", context)


def display_created_updated(request, exercise):
    if exercise == "ex07":
        return True
    return False


def populate(request, Movies, exercise="ex00", previous=None, next=None):

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

    content = []
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
            content.append(f"{title}: OK")
        except Exception as e:
            if title:
                content.append(f"{title}: {str(e)}")
            else:
                content.append(f"{str(e)}")

    context = {
        "title": get_title(exercise),
        "content": content,
        "nav_links": get_nav_links(exercise),
        "exercise": f"{exercise}",
        "previous": previous,
        "next": next,
        "active": "populate",
        "created_column": display_created_updated(request, exercise),
    }
    return render(request, "d05/templates/populate.html", context)


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
        "created_column": display_created_updated(request, exercise),
    }
    return render(request, "d05/templates/display_model.html", context)


def remove(request, Movies, exercise="ex05", previous=None, next=None):

    my_form = None

    if request.method == "GET":

        if not Movies.objects.exists():
            content = "The table does not exists"
        else:
            data = Movies.objects.all().order_by("episode_nb")
            if not data:
                content = "No data available"
            else:
                titles = []
                for movie in data:
                    titles.append(movie.title)
                my_form = RemoveMovie(
                    choices=[(title, title) for title in titles]
                )
                content = None

        context = {
            "title": get_title(exercise),
            "content": content,
            "form": my_form,
            "nav_links": get_nav_links(exercise),
            "exercise": f"{exercise}",
            "previous": previous,
            "next": next,
            "active": "remove",
            "created_column": display_created_updated(request, exercise),
        }

        return render(request, "d05/templates/remove.html", context)

    elif request.method == "POST":

        to_remove = request.POST.get("title")

        if not to_remove:
            return HttpResponseRedirect(f"/{exercise}/remove")

        if not Movies.objects.exists():
            return HttpResponseRedirect(f"/{exercise}/remove")

        to_delete = Movies.objects.filter(title=to_remove)

        if not to_delete:
            return HttpResponseRedirect(f"/{exercise}/remove")

        to_delete.delete()

        return HttpResponseRedirect(f"/{exercise}/remove")


def update(request, Movies, exercise="ex05", previous=None, next=None):

    my_form = None

    if request.method == "GET":

        if not Movies.objects.exists():
            content = "The table does not exists"
        else:
            data = Movies.objects.all().order_by("episode_nb")
            if not data:
                content = "No data available"
            else:
                titles = []
                for movie in data:
                    titles.append(movie.title)
                my_form = UpdateMovie(
                    choices=[(title, title) for title in titles]
                )
                content = None

        context = {
            "title": get_title(exercise),
            "content": content,
            "form": my_form,
            "nav_links": get_nav_links(exercise),
            "exercise": f"{exercise}",
            "previous": previous,
            "next": next,
            "active": "update",
            "created_column": display_created_updated(request, exercise),
        }

        return render(request, "d05/templates/update.html", context)

    elif request.method == "POST":

        to_update = request.POST.get("title")
        new_opening_crawl = request.POST.get("new_opening_crawl")

        if not to_update or not new_opening_crawl:
            return HttpResponseRedirect(f"/{exercise}/update")

        if not Movies.objects.exists():
            return HttpResponseRedirect(f"/{exercise}/update")

        movie = Movies.objects.filter(title=to_update).first()

        if not movie:
            return HttpResponseRedirect(f"/{exercise}/update")

        movie.opening_crawl = new_opening_crawl
        movie.save()

        return HttpResponseRedirect(f"/{exercise}/update")
