from typing import Any
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse, JsonResponse
# from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def log_in_user(request, username, password):

    """
    Log in the user and store the username in the session.
    Used by the login and register views.
    """

    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
    else:
        request.session.flush()


class Account(FormView):
    form_class = AuthenticationForm
    template_name = 'account/templates/index.html'


class Login(FormView):

    form_class = AuthenticationForm
    template_name = 'account/templates/login.html'
    success_url = "/"

    def post(self, request: HttpRequest, *args: str, **kwargs: Any):

        print("POST REQUEST RECEIVED IN LOGIN VIEW")

        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                form.cleaned_data['username'],
                form.cleaned_data['password'],
            )
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect("/account")
            else:
                print
                return JsonResponse(
                    {
                        'success': False,
                        'errors': 'Invalid username or password'
                    }
                )
        print("FORM IS NOT VALID")
        return JsonResponse(
            {
                'success': False,
                'errors': form.errors
            }
        )



class Register(CreateView):

    form_class = UserCreationForm
    template_name = 'account/templates/register.html'
    success_url = "account"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        valid = super().form_valid(form)
        if not valid:
            return JsonResponse(
                {
                    'success': False,
                    'errors': form.errors
                }
            )
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        log_in_user(self.request, username, password)
        return JsonResponse(
            {
                'success': True,
                'username': self.request.user.username
            }
        )
