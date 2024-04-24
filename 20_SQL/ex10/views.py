from django.shortcuts import render
from .forms import FormEx10
from d05.my_lib.views.sql.planets import get_nav_links
from .models import People, Movies, Planets
from django.http import HttpResponseRedirect


def empty_tables(request):
    context = {
        'title': "ex10 ORM - Many to Many",
        'nav_links': get_nav_links("ex10"),
        'form': FormEx10(),
        'previous': '/ex09/display',
        'active': 'index',
        'empty_tables': True,
    }
    return render(request, 'ex10/templates/index.html', context)


def render_form(request):
    context = {
        'title': "ex10 ORM - Many to Many",
        'nav_links': get_nav_links("ex10"),
        'form': FormEx10(),
        'previous': '/ex09/display',
        'active': 'index',
        'data': False,
    }
    return render(request, 'ex10/templates/index.html', context)


def filter_movies(min_release_date, max_release_date):
    if min_release_date and max_release_date:
        return Movies.objects.filter(
            release_date__range=[min_release_date, max_release_date]
        )
    elif min_release_date:
        return Movies.objects.filter(
            release_date__gte=min_release_date
        )
    elif max_release_date:
        return Movies.objects.filter(
            release_date__lte=max_release_date
        )
    return Movies.objects.all()


def no_results(request):
    context = {
        'title': "ex10 ORM - Many to Many",
        'nav_links': get_nav_links("ex10"),
        'form': FormEx10(),
        'previous': '/ex09/display',
        'active': 'index',
        'not_found': True
    }
    return render(request, 'ex10/templates/index.html', context)


def index(request):

    if request.method == 'GET':

        # Check if tables are empty
        # If they are not, render the search form

        if (
            People.objects.all().count() == 0 or
            Movies.objects.all().count() == 0 or
            Planets.objects.all().count() == 0
        ):
            return empty_tables(request)

        return render_form(request)

    elif request.method == 'POST':

        form = FormEx10(request.POST)

        if not form.is_valid():
            return HttpResponseRedirect('/ex10')

        min_release_date = form.cleaned_data.get('min_release_date')
        max_release_date = form.cleaned_data.get('max_release_date')
        planet_diameter = form.cleaned_data.get('planet_diameter')
        character_gender = form.cleaned_data.get('character_gender')

        movies = filter_movies(min_release_date, max_release_date)

        data = []

        # For each movie in the filtered movies (release date)
        for movie in movies:

            # For each character in the movie
            for character in movie.characters.all():

                # If the character gender corresponds to the form input
                if not character_gender or (
                    character.gender and
                    character.gender == character_gender
                ):

                    # If the character homeworld diameter is greater than or
                    # equal to the form input
                    if not planet_diameter or (
                        character.homeworld and
                        character.homeworld.diameter and
                        character.homeworld.diameter > planet_diameter
                    ):

                        # Append the character data to the data list
                        data.append({
                            'movie': movie.title,
                            'name': character.name,
                            'gender': character.gender,
                            'homeworld': character.homeworld,
                            'diameter': character.homeworld.diameter if
                            character.homeworld else None
                        })

        if not data:
            return no_results(request)

        context = {
            'title': "ex10 ORM - Many to Many",
            'nav_links': get_nav_links("ex10"),
            'form': FormEx10(),
            'previous': '/ex09/display',
            'active': 'index',
            'data': data,
            'pre_footer': True,
        }
        return render(request, 'ex10/templates/index.html', context)
