from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='chatrooms'),
    path('create/', views.CreateChatRoomView.as_view(), name='create_chatroom'),
    path('<str:room_name>/', views.ChatRoomView.as_view(), name='room'),
    path('<str:room_name>/users/', views.ChatRoomUsers, name='room_users'),
]
