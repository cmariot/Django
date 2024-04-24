import d05.my_lib.views.sql.init as sql_init
import d05.my_lib.views.sql.populate as sql_populate
import d05.my_lib.views.sql.display as sql_display


def init(request):
    return sql_init.init(
        request, "ex02", previous="/ex01/init", next="/ex03/display"
    )


def populate(request):
    return sql_populate.populate(
        request, "ex02", previous="/ex01/init", next="/ex03/display"
    )


def display(request):
    return sql_display.display(
        request, "ex02", previous="/ex01/init", next="/ex03/display"
    )
