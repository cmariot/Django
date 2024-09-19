from django.db import models


class ChatRoom(models.Model):

    id = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    users = models.ManyToManyField('account.User', related_name='chatroom_users')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):

    id = models.AutoField(primary_key=True, unique=True, editable=False)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
