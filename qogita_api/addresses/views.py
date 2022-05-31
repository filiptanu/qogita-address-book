from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from addresses.models import Address
from addresses.serializers import AddressSerializer, UserSerializer
from addresses.permissions import IsUserOrReadOnly


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
