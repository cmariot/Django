from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=64, null=False)
    author = models.ForeignKey("user.User", on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)
    synopsis = models.CharField(max_length=312, null=False)
    content = models.TextField(null=False)

    def __str__(self):
        return self.title


class UserFavoriteArticle(models.Model):

    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.article
