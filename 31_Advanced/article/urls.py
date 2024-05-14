from django.urls import path
from .views import ArticleView, PublicationsView

urlpatterns = [
    path("articles/", ArticleView.as_view(), name="articles"),
    path("publications/", PublicationsView.as_view(), name="publications"),
    # path("details/<int:pk>/", ArticleView.as_view(), name="details")
]
