from django.urls import path
from .views import dashboard, DeviceDeleteView, DeviceDetailView, DeviceListCreateView, DeviceUpdateView, MyConnectionsView


urlpatterns = [
    path('accounts/3rdparty/', MyConnectionsView.as_view(), name='socialaccount_connections'),
    path('', dashboard, name='dashboard'),
    path('device/<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('device/<int:pk>/update/', DeviceUpdateView.as_view(), name='device-update'),
    path('device/<int:pk>/delete/', DeviceDeleteView.as_view(), name='device-delete')
]
