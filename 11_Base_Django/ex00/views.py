from django.shortcuts import render


def index(request):
    """
    A view that renders the index page located at ex00/templates/index.html.

    """
    return render(request, "ex00/templates/index.html")
