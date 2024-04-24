from d05.my_lib.utils import get_nav_links, get_title
from django.shortcuts import render
from ex04.forms import RemoveMovie
from django.http import HttpResponseRedirect


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
            "created_column": True if exercise == "ex07" else False,
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
