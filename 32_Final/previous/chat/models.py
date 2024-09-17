from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):

    name = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
