import d05.my_lib.views.sql.init as sql_init
import d05.my_lib.views.sql.populate as sql_populate
import d05.my_lib.views.sql.display as sql_display
import d05.my_lib.views.sql.remove as sql_remove
import d05.my_lib.views.sql.update as sql_update


def init(request):
    return sql_init.init(
        request, "ex06", previous="/ex05/display", next="/ex07/display"
    )


def populate(request):
    return sql_populate.populate(
        request, "ex06", previous="/ex05/display", next="/ex07/display"
    )


def display(request):
    return sql_display.display(
        request, "ex06", previous="/ex05/display", next="/ex07/display"
    )


def remove(request):
    return sql_remove.remove(
        request, "ex06", previous="/ex05/display", next="/ex07/display"
    )


def update(request):
    return sql_update.update(
        request, "ex06", previous="/ex05/display", next="/ex07/display"
    )
