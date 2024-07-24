from django.urls import path
from .views import HomeView
# , SetLanguage

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # path("set_language/", SetLanguage.as_view(), name="set_language"),
]
