from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('account/', include('account.urls')),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]
