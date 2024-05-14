from django.views.generic.base import RedirectView


class HomeView(RedirectView):
    permanent = True
    query_string = True
    url = "/articles/"

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
