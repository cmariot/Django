from django.db import models


class Movies(models.Model):

    title = models.CharField(unique=True, max_length=64)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(blank=True, null=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
