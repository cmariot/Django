from django.shortcuts import render
from .models import Movies


def populate(request):
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

    # Insert data into the database using the ORM
    for data in to_insert:
        try:
            Movies.objects.create(
                episode_nb=data["episode_nb"],
                title=data["title"],
                director=data["director"],
                producer=data["producer"],
                release_date=data["release_date"]
            )
            print(f"Inserted {data}")
        except Exception as e:
            return HttpResponse(e)
            return render(request, "populate.html", {"error": e})
    return HttpResponse("OK")
    return render(request, "populate.html", {"inserted": True})


from django.http import HttpResponse

def display(request):

    # Check if the table exists
    if not Movies.objects.exists():
        return HttpResponse("No data available")

    context = {
        "data": Movies.objects.all(),
        "nav_links": {
            "populate": "/ex03/populate",
            "display": "/ex03/display",
        }
    }

    # Get all the data from the database using the ORM
    data = Movies.objects.all()
    if len(data) == 0:
        return HttpResponse("No data available")
    return render(request, "display_ex03.html", context)
