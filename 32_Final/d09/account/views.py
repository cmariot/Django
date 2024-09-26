from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.template.loader import render_to_string


class Account(FormView):

    form_class = LoginForm
    template_name = 'd09/templates/base.html'

    extra_context = {
        'title': 'Chat - Home'
    }


class Login(LoginView, FormView):

    form_class = LoginForm
    template_name = 'account/templates/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return JsonResponse({
            'success': True,
            'body': render_to_string(
                'd09/templates/body.html', request=self.request
            )
        })

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'errors': form.errors})


class Register(CreateView):

    form_class = RegisterForm
    template_name = 'account/templates/register.html'
    success_url = "/account"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        form.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return JsonResponse({
            'success': True,
            'body': render_to_string(
                'd09/templates/body.html', request=self.request
            )
        })

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'errors': form.errors})


class Logout(LogoutView):

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        logout(request)
        return JsonResponse({
            'body': render_to_string(
                'd09/templates/body.html', request=request
            )
        })
