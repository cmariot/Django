from .models import ChatRoom, Message
from django.views.generic import ListView, DetailView
from d09.settings import CHATROOMS
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


class ChatRooms(LoginRequiredMixin, ListView):

    model = ChatRoom
    template_name = 'chat/templates/chatrooms_list.html'
    context_object_name = 'chatrooms'

    login_url = '/account/'

    def get_queryset(self):
        chatrooms = ChatRoom.objects.all()
        for chatroom in CHATROOMS:
            if not ChatRoom.objects.filter(name=chatroom['name']).exists():
                ChatRoom.objects.create(
                    name=chatroom['name'],
                    description=chatroom['description']
                )
        return chatrooms

    def get_redirect_field_name(self) -> str:
        return ""


class Chat(LoginRequiredMixin, DetailView):

    model = ChatRoom
    template_name = 'chat/templates/chat.html'
    context_object_name = 'chat'
    slug_field = 'name'
    slug_url_kwarg = 'room_name'

    login_url = '/account/'

    def get_redirect_field_name(self) -> str:
        return ""


def get_chatroom_users(request, room_name):

    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'})

    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'})

    chatroom = ChatRoom.objects.get(name=room_name)
    users = chatroom.users.all().order_by('username')
    users_list = []
    for user in users:
        users_list.append(user.username)
    return JsonResponse(users_list, safe=False)


def get_chatroom_messages(request, room_name):

    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'})

    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'})

    chatroom = ChatRoom.objects.get(name=room_name)
    if not chatroom:
        return JsonResponse({'error': 'Chatroom not found'})

    messages = Message.objects.filter(chatroom=chatroom)
    messages = messages.order_by('created_at')
    messages_list = []

    for message in messages:
        messages_list.append({
            'id': message.id,
            'user': message.user.username,
            'content': message.content,
            'created_at': message.created_at.astimezone().strftime(
                '%m/%d/%Y %H:%M:%S'
            )
        })

    return JsonResponse(messages_list[-3:], safe=False)
