import d05.my_lib.views.orm.populate as orm_populate
import d05.my_lib.views.orm.display as orm_display
from .models import Movies


def populate(request):
    return orm_populate.populate(
        request, Movies, exercise="ex03",
        previous="/ex02/display", next="/ex04/display"
    )


def display(request):
    return orm_display.display(
        request, Movies, exercise="ex03",
        previous="/ex02/display", next="/ex04/display"
    )
