from django.shortcuts import render


def index(request):
    return render(request, "ex00/templates/index.html")
