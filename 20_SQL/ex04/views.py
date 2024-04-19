import d05.my_lib.sql as d05


def init(request):
    return d05.init(
        request, "ex04", previous="/ex03/display", next="/ex05/display"
    )


def populate(request):
    return d05.populate(
        request, "ex04", previous="/ex03/display", next="/ex05/display"
    )


def display(request):
    return d05.display(
        request, "ex04", previous="/ex03/display", next="/ex05/display"
    )


def remove(request):
    return d05.remove(
        request, "ex04", previous="/ex03/display", next="/ex05/display"
    )