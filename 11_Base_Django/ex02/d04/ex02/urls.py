from django.urls import path

from . import views

urlpatterns = [
    path("form", views.form, name="form"),
    path("save", views.save, name="save"),
    path("result", views.result, name="result"),
]
