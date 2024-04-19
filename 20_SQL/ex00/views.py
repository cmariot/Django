import d05.my_lib.sql


def init(request):
    return d05.my_lib.sql.init(request, "ex00", next="/ex02/display")
