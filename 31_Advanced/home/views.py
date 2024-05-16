from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView
from .forms.SetLanguageForm import SetLanguageForm
from django.conf import settings

class HomeView(RedirectView):
    permanent = True
    query_string = True
    url = "/articles/"

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)


class SetLanguage(FormView):
    form_class = SetLanguageForm
    template_name = "home/templates/set_language.html"
    success_url = "/"

    def form_valid(self, form):
        lang = form.cleaned_data["lang"]
        settings.LANGUAGE_CODE = lang
        return super().form_valid(form)
