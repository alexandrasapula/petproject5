from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.models import Device
from .models import Message
from .services.chat_engine import chat_engine


class ChatAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get("message")
        device_id = request.data.get("device_id")
        device = Device.objects.get(id=device_id, user=request.user)

        Message.objects.create(user=request.user, device=device, content=message, is_bot=False)
        messages = Message.objects.filter(user=request.user, device=device)
        bot_response = chat_engine(device, message, messages)
        # bot_response = f"{message}"
        Message.objects.create(user=request.user, device=device, content=bot_response, is_bot=True)

        return Response({
            "answer": bot_response,
            "device_model": device.model,
            "device_id": device_id
            })

    def get(self, request):
        device_id = request.GET.get('device_id')
        device = Device.objects.get(id=device_id, user=request.user)
        messages = Message.objects.filter(user=request.user, device=device)
        data = [{
            "content": msg.content,
            "is_bot": msg.is_bot,
            "timestamp": msg.timestamp
        } for msg in messages]
        return Response(data)
