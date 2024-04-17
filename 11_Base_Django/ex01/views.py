from django.shortcuts import render


def get_nav_links():
    return {
        "Django": "/ex01/django",
        "Affichage": "/ex01/affichage",
        "Templates": "/ex01/templates",
    }


def django(request):
    context = {
        "style": 1,
        "nav_links": get_nav_links(),
    }
    return render(request, "ex01/templates/django.html", context)


def affichage(request):
    context = {
        "style": 1,
        "nav_links": get_nav_links(),
    }
    return render(request, "ex01/templates/affichage.html", context)


def templates(request):
    context = {
        "style": 2,
        "nav_links": get_nav_links(),
    }
    return render(request, "ex01/templates/templates.html", context)
