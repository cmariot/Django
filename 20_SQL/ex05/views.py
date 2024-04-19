import d05.my_lib.model as model


def populate(request):
    return model.populate(
        request, exercise="ex05", previous="/ex04/display", next="/ex06/display"
    )


def display(request):
    return model.display(
        request, exercise="ex05", previous="/ex04/display", next="/ex06/display"
    )

def remove(request):
    return model.remove(
        request, exercise="ex05", previous="/ex04/display", next="/ex06/display"
    )