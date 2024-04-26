from django.db import models
from user.models import User
from django.core import validators


class Tip(models.Model):

    """
    Tip is a model for storing tips.
    """

    # Tip model main fields
    id = models.AutoField(primary_key=True, unique=True)
    content = models.TextField(
        validators=[
            validators.MinLengthValidator(1),
            validators.MaxLengthValidator(1000),
        ]
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Up-votes and down-votes
    up = models.ManyToManyField(User, related_name="up")
    down = models.ManyToManyField(User, related_name="down")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
