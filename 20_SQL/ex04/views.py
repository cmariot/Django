import d05.my_lib.views.sql.display as sql_display
import d05.my_lib.views.sql.init as sql_init
import d05.my_lib.views.sql.populate as sql_populate
import d05.my_lib.views.sql.remove as sql_remove


def init(request):
    return sql_init.init(
        request, "ex04", previous="/ex03/display", next="/ex05/display"
    )


def populate(request):
    return sql_populate.populate(
        request, "ex04", previous="/ex03/display", next="/ex05/display"
    )


def display(request):
    return sql_display.display(
        request, "ex04", previous="/ex03/display", next="/ex05/display"
    )


def remove(request):
    return sql_remove.remove(
        request, "ex04", previous="/ex03/display", next="/ex05/display"
    )
