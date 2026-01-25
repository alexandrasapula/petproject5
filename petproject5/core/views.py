from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.views import ConnectionsView
from rest_framework import generics, permissions
from .models import Device
from .serializers import DeviceSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from manuals.services.process_manual import process_manual


@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


class DeviceListCreateView(generics.ListCreateAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        device = serializer.save(user=self.request.user)

        if device.manual:
            process_manual(device)


class DeviceDetailView(generics.RetrieveAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)


class DeviceUpdateView(generics.UpdateAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        device = serializer.save()

        if device.manual:
            process_manual(device)


class DeviceDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)


class MyConnectionsView(ConnectionsView):
    def get(self, *args, **kwargs):
        return redirect('/')
