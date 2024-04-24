from d05.my_lib.utils import get_nav_links, get_title
from django.shortcuts import render


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
        "created_column": True if exercise == "ex07" else False,
    }
    return render(request, "d05/templates/populate.html", context)
