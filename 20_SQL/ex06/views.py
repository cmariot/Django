import d05.my_lib.sql as d05


def init(request):
    return d05.init(
        request, "ex06", previous="/ex05/display", next="/ex07/display"
    )


def populate(request):
    return d05.populate(
        request, "ex06", previous="/ex05/display", next="/ex07/display"
    )


def display(request):
    return d05.display(
        request, "ex06", previous="/ex05/display", next="/ex07/display"
    )


def remove(request):
    return d05.remove(
        request, "ex06", previous="/ex05/display", next="/ex07/display"
    )


def update(request):
    return d05.update(
        request, "ex06", previous="/ex05/display", next="/ex07/display"
    )
