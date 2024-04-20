import d05.my_lib.model as model
from .models import Movies


def populate(request):
    return model.populate(
        request, Movies, exercise="ex03",
        previous="/ex02/display", next="/ex04/display"
    )


def display(request):
    return model.display(
        request, Movies, exercise="ex03",
        previous="/ex02/display", next="/ex04/display"
    )
