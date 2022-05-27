from rest_framework import serializers
from addresses.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['uuid', 'street_name', 'street_number', 'zip_code', 'city', 'country']
