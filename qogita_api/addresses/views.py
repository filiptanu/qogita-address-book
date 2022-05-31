from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from addresses.models import Address
from addresses.serializers import AddressSerializer, DeleteManyAddressesSerializer, UserSerializer
from addresses.permissions import IsUserOrReadOnly


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['POST'])
def delete_many(request):
    serializer = DeleteManyAddressesSerializer(data=request.data)
    if serializer.is_valid():
        uuids = request.data.get('uuids')

        addresses_to_delete = Address.objects.filter(uuid__in=uuids)
        addresses_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
