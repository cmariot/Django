from django.urls import re_path
from .consumers import ChatRoomConsumer


# URLs that handle the WebSocket connection are placed here.
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatRoomConsumer.as_asgi()),
]
