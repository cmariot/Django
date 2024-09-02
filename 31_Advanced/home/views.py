from django.views.generic.base import RedirectView


class HomeView(RedirectView):
    permanent = False
    url = "/articles/"

    def get_redirect_url(self, *args, **kwargs):
        """
        Redirect to the articles page in the user's language.
        """
        language = self.request.LANGUAGE_CODE
        if not language:
            language = "en"
        self.url = f"/{language}/articles/"
        return super().get_redirect_url(*args, **kwargs)
