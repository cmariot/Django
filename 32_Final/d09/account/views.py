from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class Account(FormView):
    form_class = AuthenticationForm
    template_name = 'account/templates/index.html'


class Login(FormView):

    form_class = AuthenticationForm
    template_name = 'account/templates/login.html'

    def form_valid(self, form):
        print("The login form is valid.")
        login(self.request, form.get_user())
        return JsonResponse(
            {
                'success': True,
                'errors': {},
                'username': self.request.user.username
            }
        )

    def form_invalid(self, form):
        print("The login form is not valid.")
        return JsonResponse(
            {
                'success': False,
                'errors': form.errors
            }
        )


class Register(CreateView):

    form_class = UserCreationForm
    template_name = 'account/templates/register.html'
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        print("The register form is valid.")
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def form_invalid(self, form):
        print("The register form is not valid.")
        return JsonResponse(
            {
                'success': False,
                'errors': form.errors
            }
        )
