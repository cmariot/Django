import d05.my_lib.model as model


def init(request):
    return model.init(
        request, "ex01", previous="/ex00/init", next="/ex02/display"
    )
