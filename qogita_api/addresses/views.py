from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from addresses.models import Address
from addresses.serializers import AddressSerializer


class AddressList(APIView):
    def get(self, request, format=None):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressDetail(APIView):
    def get_object(self, address_uuid):
        try:
            return Address.objects.get(uuid=address_uuid)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, address_uuid, format=None):
        address = self.get_object(address_uuid)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, address_uuid, format=None):
        address = self.get_object(address_uuid)
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, address_uuid, format=None):
        address = self.get_object(address_uuid)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
