from django.urls import path

from . import views

urlpatterns = [
    path("django", views.django, name="django"),
    path("affichage", views.affichage, name="affichage"),
    path("templates", views.templates, name="templates")
]
