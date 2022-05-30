from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from addresses.models import Address
from django.contrib.auth.models import User


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Address
        fields = ['uuid', 'street_name', 'street_number', 'zip_code', 'city', 'country', 'user']


class UserSerializer(serializers.ModelSerializer):
    addresses = serializers.PrimaryKeyRelatedField(many=True, queryset=Address.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'addresses']
