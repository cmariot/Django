from .models import ChatRoom
from django.views.generic import ListView, DetailView
from d09.settings import CHATROOMS


class ChatRooms(ListView):

    model = ChatRoom
    template_name = 'chat/templates/chatrooms_list.html'
    context_object_name = 'chatrooms'

    def get_queryset(self):
        chatrooms = ChatRoom.objects.all()
        for chatroom in CHATROOMS:
            if not ChatRoom.objects.filter(name=chatroom['name']).exists():
                ChatRoom.objects.create(
                    name=chatroom['name'],
                    description=chatroom['description']
                )
        return chatrooms


class Chat(DetailView):

    model = ChatRoom
    template_name = 'chat/templates/chat.html'
    context_object_name = 'chat'
    slug_field = 'name'
    slug_url_kwarg = 'room_name'
