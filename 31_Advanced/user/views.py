from django.http import HttpResponseRedirect
from user.forms.register_form import RegisterForm
from user.forms.login import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.generic.edit import FormView, CreateView
from .forms.logout import LogoutForm
from django.utils.translation import gettext_lazy as _


LOGGED_IN_SESSION_TIMEOUT = 60 * 60 * 24 * 7


def log_in_user(request, username, password):

    """
    Log in the user and store the username in the session.
    Used by the login and register views.
    """

    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        request.session.set_expiry(LOGGED_IN_SESSION_TIMEOUT)
    else:
        request.session.flush()


class RegisterUser(CreateView):

    form_class = RegisterForm
    template_name = "user/templates/register.html"
    success_url = "/"

    extra_context = {
        'Username': _('Username'),
        'Password': _('Password'),
        'Password confirmation': _('Password confirmation'),
        'Register': _('Register'),
        'Already have an account?': _('Already have an account?'),
        'Login': _('Login'),
        'Create an account': _('Create an account'),
    }

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if form.cleaned_data.get('password') != form.cleaned_data.get('confirmation'):
            form.add_error('confirmation', _('The passwords do not match.'))
            return self.form_invalid(form)
        valid = super().form_valid(form)
        if not valid:
            return valid
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        log_in_user(self.request, username, password)
        return valid


class LoginUser(FormView):

    template_name = "user/templates/login.html"
    form_class = LoginForm
    success_url = "/"

    extra_context = {
        'Login': _('Login'),
        'Access your account': _('Access your account'),
        'Username': _('Username'),
        'Password': _('Password'),
        "Don't have an account?": _("Don't have an account?"),
        'Register': _('Register'),
    }

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        valid = super(LoginUser, self).form_valid(form)
        if not valid:
            return valid
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        log_in_user(self.request, username, password)
        return valid


class LogoutUser(FormView):

    form_class = LogoutForm
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        valid = super(LogoutUser, self).form_valid(form)
        if not valid:
            return valid
        if self.request.user.is_authenticated:
            auth_logout(self.request)
        self.request.session.flush()
        return HttpResponseRedirect("/")
