from channels.generic.websocket import AsyncWebsocketConsumer
import json
from datetime import datetime


class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Join the channel group
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the channel group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.scope['user'].username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Envoyer le message WebSocket au client
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'username': username,
            'message': message,
            'datetime': str(datetime.now().strftime('%m/%d/%Y %H:%M'))
        }))
