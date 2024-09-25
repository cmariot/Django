from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import ChatRoom, Message
from account.models import User
from asgiref.sync import sync_to_async


def save_message(username, room_name, content):
    chatroom = ChatRoom.objects.get(name=room_name)
    if not chatroom:
        return
    user = User.objects.get(username=username)
    if not user:
        return
    message = Message.objects.create(
        chatroom=chatroom,
        user=user,
        content=content
    )
    return message


def add_user(username, room_name):
    chat_room = ChatRoom.objects.get(name=room_name)
    if not chat_room:
        return
    elif chat_room.users.filter(username=username).exists():
        return
    user = User.objects.get(username=username)
    if not user:
        return
    chat_room.users.add(user)
    chat_room.save()


def remove_user(username, room_name):
    chat_room = ChatRoom.objects.get(name=room_name)
    if not chat_room:
        return
    elif not chat_room.users.filter(username=username).exists():
        return
    user = User.objects.get(username=username)
    if not user:
        return
    chat_room.users.remove(user)
    chat_room.save()


class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.username = self.scope['user'].username
        await sync_to_async(add_user)(self.username, self.room_name)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_connection',
                'username': self.username
            }
        )
        await self.accept()

    async def disconnect(self, close_code):
        await sync_to_async(remove_user)(self.username, self.room_name)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_disconnection',
                'username': self.username
            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.scope['user'].username
        message_saved = await sync_to_async(save_message)(
            username, self.room_name, message
        )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'id': message_saved.id,
                'message': message_saved.content,
                'username': message_saved.user.username,
                'datetime': str(
                    message_saved.created_at
                        .astimezone()
                        .strftime('%m/%d/%Y %H:%M:%S')
                ),
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'username': event['username'],
            'message': event['message'],
            'datetime': event['datetime'],
            'id': event['id']
        }))

    async def chat_connection(self, event):
        await self.send(text_data=json.dumps({
            'type': 'chat_connection',
            'username': event['username']
        }))

    async def chat_disconnection(self, event):
        await self.send(text_data=json.dumps({
            'type': 'chat_disconnection',
            'username': event['username']
        }))
