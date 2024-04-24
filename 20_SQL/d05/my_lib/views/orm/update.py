from d05.my_lib.utils import get_nav_links, get_title
from django.shortcuts import render
from ex06.forms import UpdateMovie
from django.http import HttpResponseRedirect


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
            "created_column": True if exercise == "ex07" else False,
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
