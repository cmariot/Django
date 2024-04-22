from django.shortcuts import render
from .models import Planets, People


def display(request):

    # Cette vue doit afficher dans un tableau HTML tous les noms de personnages,
    # leur planète d’origine ainsi que le climat, dont ledit climat est tout ou
    # partie venteux (’windy’), trié par ordre alphabetique des noms de
    # personnages.

    data = People.objects.filter(homeworld__climate__icontains="windy").order_by("name")
    return render(request, "d05/templates/display_model.html", {"data": data})

    # https://haddad-tech.medium.com/automatic-data-seeding-using-csv-and-custom-django-admin-command-99b6c3aad819