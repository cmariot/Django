from django.urls import path
from .views import ChatRooms, Chat, get_chatroom_users, get_chatroom_messages

urlpatterns = [
    path(
        '',
        ChatRooms.as_view(),
        name='chatrooms'
    ),
    path(
        '<str:room_name>/',
        Chat.as_view(),
        name='chat'
    ),
    path(
        '<str:room_name>/users/',
        get_chatroom_users,
        name='chatroom_users'
    ),
    path(
        '<str:room_name>/messages/',
        get_chatroom_messages,
        name='chatroom_messages'
    ),
]
