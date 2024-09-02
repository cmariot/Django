import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, ChatRoom
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
from threading import Thread


class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.chat_box_name = self.scope["url_route"]["kwargs"]["chat_box_name"]
        self.group_name = "chat_%s" % self.chat_box_name
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        # Notify everyone in the room that a user has joined
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_connection",
                "username": self.scope["user"].username,
            },
        )

        # Send last 3 messages to the user
        messages = await sync_to_async(Message.objects.filter)(
            chatroom__name=self.chat_box_name
        )
        messages = await sync_to_async(list)(messages.order_by("-timestamp")[:3])
        for i in range(len(messages) - 1, -1, -1):
            username = await sync_to_async(User.objects.get)(
                id=messages[i].user_id
            )
            username = username.username
            await self.send(
                text_data=json.dumps(
                    {
                        "type": "chat_message",
                        "username": username,
                        "message": messages[i].message,
                    }
                )
            )

        # Save the User in the chat room
        chatroom = await sync_to_async(
            ChatRoom.objects.get)(name=self.chat_box_name)
        user = await sync_to_async(
            User.objects.get)(username=self.scope["user"].username)
        await sync_to_async(chatroom.users.add)(user)

        # Notify the user of the other users in the chat room in a thread
        def notify_user():
            users = chatroom.users.all()
            for user in users:
                if user.username != self.scope["user"].username:
                    self.channel_layer.group_send(
                        self.group_name,
                        {
                            "type": "chat_connection",
                            "username": user.username,
                        },
                    )

        Thread(target=notify_user).start()

    async def disconnect(self, close_code):

        # Notify everyone in the room that a user has left
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_disconnect",
                "username": f"{self.scope['user'].username}",
            },
        )
        await self.channel_layer.group_discard(
            self.group_name, self.channel_name
        )

        # Remove the User from the chat room
        chatroom = await sync_to_async(
            ChatRoom.objects.get)(name=self.chat_box_name)
        user = await sync_to_async(
            User.objects.get)(username=self.scope["user"].username)
        await sync_to_async(chatroom.users.remove)(user)

    async def receive(self, text_data):

        text_data_json = json.loads(text_data)

        message = text_data_json["message"]
        username = text_data_json["username"]

        # Avoid XSS attacks
        message = message.replace("<", "&lt;").replace(">", "&gt;")
        username = username.replace("<", "&lt;").replace(">", "&gt;")

        # Avoid empty messages
        message = message.strip()
        if not message:
            return

        # Save message to database
        chatroom = await sync_to_async(ChatRoom.objects.get)(
            name=self.chat_box_name
        )
        user = await sync_to_async(User.objects.get)(username=username)
        if not user or not chatroom:
            return

        await sync_to_async(Message.objects.create)(
            chatroom=chatroom, user=user, message=message
        )

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",
                "username": username,
                "message": message,
            },
        )

    # Receive message from room group.
    async def chat_message(self, event):

        message = event["message"]
        username = event["username"]

        await self.send(
            text_data=json.dumps(
                {
                    "type": "chat_message",
                    "username": username,
                    "message": message,
                }
            )
        )

    async def chat_connection(self, event):

        username = event["username"]

        await self.send(
            text_data=json.dumps(
                {
                    "type": "chat_connection",
                    "username": username,
                }
            )
        )

    async def chat_disconnect(self, event):

        username = event["username"]

        await self.send(
            text_data=json.dumps(
                {
                    "type": "chat_disconnect",
                    "username": username,
                }
            )
        )
