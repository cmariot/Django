from django.db import models


class ChatRoom(models.Model):

    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    users = models.ManyToManyField('account.User', related_name='chatroom_users')

    def __str__(self):
        return self.name


class Message(models.Model):

    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
