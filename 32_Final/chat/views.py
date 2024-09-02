from .models import ChatRoom
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

# ChatRoom is a model that represents a chat room.
# The IndexView is a view that lists all chat rooms.
# The ChatRoomView is a view that displays a chat room.


@method_decorator(login_required(login_url="account"), name='dispatch')
class IndexView(ListView):

    model = ChatRoom
    template_name = 'index.html'
    context_object_name = 'chatrooms'


@method_decorator(login_required(login_url="account"), name='dispatch')
class ChatRoomView(DetailView):

    model = ChatRoom
    template_name = 'chat_room.html'
    context_object_name = 'chatroom'
    slug_field = 'name'
    slug_url_kwarg = 'room_name'


@method_decorator(login_required(login_url="account"), name='dispatch')
class CreateChatRoomView(CreateView):

    model = ChatRoom
    fields = ['name']
    template_name = 'create_chatroom.html'
    success_url = reverse_lazy('chatrooms')


def ChatRoomUsers(request, room_name):

    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'})

    chatroom = ChatRoom.objects.get(name=room_name)
    users = chatroom.users.all()
    usernames = [user.username for user in users]
    return JsonResponse({'users': usernames})
