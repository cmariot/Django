import d05.my_lib.views.orm.display as orm_display
import d05.my_lib.views.orm.populate as orm_populate
import d05.my_lib.views.orm.remove as orm_remove
import d05.my_lib.views.orm.update as orm_update
from .models import Movies


def populate(request):
    return orm_populate.populate(
        request, Movies, exercise="ex07",
        previous="/ex06/display", next="/ex08/display"
    )


def display(request):
    return orm_display.display(
        request, Movies, exercise="ex07",
        previous="/ex06/display", next="/ex08/display"
    )


def remove(request):
    return orm_remove.remove(
        request, Movies, exercise="ex07",
        previous="/ex06/display", next="/ex08/display"
    )


def update(request):
    return orm_update.update(
        request, Movies, exercise="ex07",
        previous="/ex06/display", next="/ex08/display"
    )
