from django.urls import path
from .views import ChatAPIView


urlpatterns = [
    path('send/', ChatAPIView.as_view(), name='chat-send'),
]
