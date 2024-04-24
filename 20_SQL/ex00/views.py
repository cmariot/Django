import d05.my_lib.views.sql.init as sql_init


def init(request):
    return sql_init.init(request, "ex00", next="/ex01/init")
