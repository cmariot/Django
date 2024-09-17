from django.urls import path
from .views import AccountView, LogoutView, RegisterView

urlpatterns = [
    path('', AccountView.as_view(), name='account'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
