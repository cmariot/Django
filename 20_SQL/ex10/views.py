from django.shortcuts import render
from .forms import FormEx10
from d05.my_lib.sql import get_nav_links


def index(request):

    if request.method == 'GET':

        context = {
            'title': "ex10 ORM - Many to Many",
            'nav_links': get_nav_links("ex10"),
            'form': FormEx10(),
            'previous': '/ex09/display',
            'active': 'index'
        }
        return render(request, 'ex10/templates/index.html', context)

    elif request.method == 'POST':

        form = FormEx10(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

        min_release_date = form.cleaned_data.get('min_release_date')
        max_release_date = form.cleaned_data.get('max_release_date')
        planet_diameter = form.cleaned_data.get('planet_diameter')
        character_gender = form.cleaned_data.get('character_gender')

        print(min_release_date)
        print(max_release_date)
        print(planet_diameter)
        print(character_gender)

        context = {
        }
        return render(request, 'ex10/templates/index.html', context)

