from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    id = models.AutoField(primary_key=True, unique=True, editable=False)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username
