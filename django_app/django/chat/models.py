from django.db import models


class Message(models.Model):
    """
    Message is a model for chat messages.
    """

    content = models.TextField(
        max_length=1000,
        blank=False,
        null=False,
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    def __str__(self):
        return self.content
