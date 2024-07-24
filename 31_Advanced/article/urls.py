from django.urls import path
from .views import (
    ArticleDetail, UserArticles, ArticleList,
    PublishArticle, AddToFav, UserFavoriteArticles, RemoveFromFav
)

urlpatterns = [
    path("articles/", ArticleList.as_view(), name="articles"),
    path("publications/", UserArticles.as_view(), name="publications"),
    path("articles/<int:pk>/", ArticleDetail.as_view(), name="details"),
    path("publish/", PublishArticle.as_view(), name="publish"),
    path("articles/<int:pk>/add_to_fav/", AddToFav.as_view(), name="add_to_favorites"),
    path("articles/<int:article_id>/remove_from_fav/", RemoveFromFav.as_view(), name="remove_from_favorites"),
    path("favorites/", UserFavoriteArticles.as_view(), name="favorites"),
]
