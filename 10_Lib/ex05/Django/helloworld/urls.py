from django.urls import path

from . import views

# urlpatterns list routes URLs to views.
# It's included in the Django project's urls.py file.

urlpatterns = [
    path(
        route="",           # URL pattern
        view=views.index,   # View function
        name="index"        # Name of the URL pattern
    ),
]
