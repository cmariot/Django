from django.urls import path
from .views import ChatRooms, Chat

urlpatterns = [
    path('', ChatRooms.as_view(), name='chatrooms'),
    path('<slug:slug>/', Chat.as_view(), name='chat'),
]
