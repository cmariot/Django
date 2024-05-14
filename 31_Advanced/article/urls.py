from django.urls import path
from .views import ArticleDetail, UserArticles, ArticleList

urlpatterns = [
    path("articles/", ArticleList.as_view(), name="articles"),
    path("publications/", UserArticles.as_view(), name="publications"),
    path("articles/<int:pk>/", ArticleDetail.as_view(), name="details")
]
