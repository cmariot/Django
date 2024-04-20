import d05.my_lib.model as model
from .models import Movies


def populate(request):
    return model.populate(
        request, Movies, exercise="ex07",
        previous="/ex06/display", next="/ex08/display"
    )


def display(request):
    return model.display(
        request, Movies, exercise="ex07",
        previous="/ex06/display", next="/ex08/display"
    )


def remove(request):
    return model.remove(
        request, Movies, exercise="ex07",
        previous="/ex06/display", next="/ex08/display"
    )


def update(request):
    return model.update(
        request, Movies, exercise="ex07",
        previous="/ex06/display", next="/ex08/display"
    )
