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
    chatroom = ChatRoom.objects.get(name=room_name)
    users = chatroom.users.all()
    users_list = []
    for user in users:
        users_list.append(user.username)
    return JsonResponse(users_list, safe=False)


def get_chatroom_messages(request, room_name):

    print('get_chatroom_messages, room_name:', room_name)

    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'})

    chatroom = ChatRoom.objects.get(name=room_name)
    if not chatroom:
        return JsonResponse({'error': 'Chatroom not found'})

    messages = Message.objects.filter(chatroom=chatroom)
    messages = messages.order_by('created_at')
    messages_list = []

    # If first message id is provided, return 10 messages before that message
    first_message_id = request.GET.get('first_message_id')
    if first_message_id:
        for message in messages:
            if message.id == int(first_message_id):
                break
            messages_list.append({
                'id': message.id,
                'user': message.user.username,
                'content': message.content,
                'created_at': message.created_at.strftime('%m/%d/%Y %H:%M')
            })
        return JsonResponse(messages_list[-10:], safe=False)

    for message in messages:
        messages_list.append({
            'id': message.id,
            'user': message.user.username,
            'content': message.content,
            'created_at': message.created_at.strftime('%m/%d/%Y %H:%M')
        })

    return JsonResponse(messages_list[-3:], safe=False)
