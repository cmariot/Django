import d05.my_lib.model as model


def populate(request):
    return model.populate(
        request, exercise="ex03", previous="/ex02/display", next="/ex04/display"
    )


def display(request):
    return model.display(
        request, exercise="ex03", previous="/ex02/display", next="/ex04/display"
    )
