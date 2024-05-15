from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("username/", views.get_username, name="get_username"),
]
