from django.contrib import admin
from .models import Article, UserFavoriteArticle


admin.site.register(Article)
admin.site.register(UserFavoriteArticle)
