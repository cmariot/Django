from django.shortcuts import render


def django(request):
    context = {
        "style": "style1.css",
    }
    return render(request, "django.html", context)


def affichage(request):
    context = {
        "style": "style1.css",
    }
    return render(request, "affichage.html", context)


def templates(request):
    context = {
        "style": "style1.css",
    }
    return render(request, "templates.html", context)
