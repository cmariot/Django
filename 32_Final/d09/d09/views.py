from django.views.generic.base import RedirectView


class HomeView(RedirectView):
    url = '/account'
    permanent = True
