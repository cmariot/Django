import d05.my_lib.model as model
from .models import Movies


def populate(request):
    return model.populate(
        request, Movies, exercise="ex05",
        previous="/ex04/display", next="/ex06/display"
    )


def display(request):
    return model.display(
        request, Movies, exercise="ex05",
        previous="/ex04/display", next="/ex06/display"
    )


def remove(request):
    return model.remove(
        request, Movies, exercise="ex05",
        previous="/ex04/display", next="/ex06/display"
    )
