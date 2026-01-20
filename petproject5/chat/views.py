from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.models import Device


class ChatAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get("message")
        device_id = request.data.get('device_id')
        device = Device.objects.get(id=device_id, user=request.user)
        return Response({
            "answer": f"{message}",
            "device_id": device_id,
            "device_model": device.model,
            })
