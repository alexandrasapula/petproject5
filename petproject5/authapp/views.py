from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request, user)

        return Response({"redirect": "/"}, status=201)


@api_view(['POST'])
def LoginView(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"redirect": "/"}, status=201)
    else:
        return Response({"error": "Неверный логин или пароль"}, status=400)


def auth_page(request):
    return render(request, "authapp/auth.html")
