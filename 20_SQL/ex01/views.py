import d05.my_lib.views.orm.init as orm_init


def init(request):
    return orm_init.init(
        request, "ex01", previous="/ex00/init", next="/ex02/display"
    )
