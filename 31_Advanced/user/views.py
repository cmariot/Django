from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from user.forms.register_form import RegisterForm
from user.forms.login import LoginForm
from .models import User
import random
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



ANONYMOUS_SESSION_TIMEOUT = 42
LOGGED_IN_SESSION_TIMEOUT = 60 * 60 * 24 * 7
ANONYMOUS_USERNAMES = [
    "Anonymous",
    "AnonymousUser",
    "Anon",
    "AnonUser",
    "Anon"
]


def get_user_data(request):

    """
    Get the user data and return it in a dictionary.
    The dictionary is used to render the templates.
    """

    is_logged_in = False
    if request.user.is_authenticated:
        username = request.user.username
        is_logged_in = True
    else:
        if "username" not in request.session:
            username = random.choice(ANONYMOUS_USERNAMES)
            request.session["username"] = username
            request.session.set_expiry(ANONYMOUS_SESSION_TIMEOUT)
        else:
            username = request.session["username"]
    context = {
        "username": username,
        "is_logged_in": is_logged_in,
    }
    return context


def log_in_user(request, username, password):

    """
    Log in the user and store the username in the session.
    Used by the login and register views.
    """

    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        request.session["username"] = username
        request.session["is_logged_in"] = True
        request.session.set_expiry(LOGGED_IN_SESSION_TIMEOUT)
    else:
        request.session.flush()


def logout(request):

    """
    Log out the user and redirect to the home page.
    The session is flushed to remove the username.
    """

    if request.user.is_authenticated:
        auth_logout(request)
    request.session.flush()
    return HttpResponseRedirect("/")


# def register(request):

#     # If the user is already logged in, redirect to the home page
#     if request.user.is_authenticated:
#         return HttpResponseRedirect("/")

#     # Get method : display the register form
#     elif request.method == "GET":
#         context = get_user_data(request)
#         context["form"] = RegisterForm()
#         return render(request, "user/templates/register.html", context)

#     # Post method : process the register form
#     elif request.method == "POST":
#         form = RegisterForm(request.POST)
#         if not form.is_valid():
#             context = get_user_data(request)
#             context["form"] = form
#             return render(request, "user/templates/register.html", context)
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data["password"]
#         user = User.objects.create_user(username, password=password)
#         user.save()
#         log_in_user(request, username, password)
#         return HttpResponseRedirect("/")


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "user/templates/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        valid = super(RegisterView, self).form_valid(form)
        if not valid:
            return valid
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        log_in_user(self.request, username, password)
        return valid


def login(request):

    """
    Log in the user and store the username in the session.
    """

    # If the user is already logged in, redirect to the home page
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")

    # Get method : display the login form
    if request.method == "GET":

        context = get_user_data(request)
        context["form"] = LoginForm()
        return render(request, "user/templates/login.html", context)

    # Post method : process the login form
    elif request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            log_in_user(request, username, password)
            return HttpResponseRedirect("/")

        # If the form is not valid, display the login form with the errors
        context = get_user_data(request)
        context["form"] = form
        return render(request, "user/templates/login.html", context)


def get_username(request):
    """

    Used to get the username of the current user. If the user is not logged in,
    a random username is generated and stored in the session.

    ANONYMOUS_USERNAMES is a list of possible usernames for anonymous users.
    ANONYMOUS_SESSION_TIMEOUT = 42 seconds

    """
    if request.user.is_authenticated:
        username = request.user.username
    elif "username" in request.session:
        username = request.session["username"]
    else:
        username = random.choice(ANONYMOUS_USERNAMES)
        request.session["username"] = username
        request.session.set_expiry(ANONYMOUS_SESSION_TIMEOUT)
    return HttpResponse(username)
