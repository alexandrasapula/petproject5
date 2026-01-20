from django.urls import path
from .views import RegisterView, LoginView, auth_page

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView, name='login'),

    path('', auth_page, name="auth"),
]
