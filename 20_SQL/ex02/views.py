import d05.my_lib.sql


def init(request):
    return d05.my_lib.sql.init(
        request, "ex02", previous="/ex00/init", next="/ex03/display"
    )


def populate(request):
    return d05.my_lib.sql.populate(
        request, "ex02", previous="/ex00/init", next="/ex03/display"
    )


def display(request):
    return d05.my_lib.sql.display(
        request, "ex02", previous="/ex00/init", next="/ex03/display"
    )
