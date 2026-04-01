from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.serializers import UserRegistrationSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
