from d05.my_lib.views.sql.planets import (
    init_planets, populate_planets, display_planets
)


def init(request):
    return init_planets(request)


def populate(request):
    return populate_planets(request)


def display(request):
    return display_planets(request)
