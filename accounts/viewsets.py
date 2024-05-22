from rest_framework import viewsets

from accounts.permissions import UserPermissions
from .models import CustomUser
from .serializers import CustomUserSerializer, ContactSerializer

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (UserPermissions, )