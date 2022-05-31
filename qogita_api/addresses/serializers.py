from rest_framework import serializers
from addresses.models import Address
from django.contrib.auth.models import User
from uuid import UUID


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Address
        fields = ['uuid', 'street_name', 'street_number', 'zip_code', 'city', 'country', 'user']


class DeleteManyAddressesSerializer(serializers.Serializer):
    uuids = serializers.ListField(child=serializers.CharField())

    def validate_uuids(self, uuids):
        for uuid in uuids:
            try:
                UUID(uuid, version=4)
            except ValueError:
                raise exceptions.ValidationError("Invalid address UUID: " + uuid)
                
        return uuids


class UserSerializer(serializers.ModelSerializer):
    addresses = serializers.PrimaryKeyRelatedField(many=True, queryset=Address.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'addresses']
