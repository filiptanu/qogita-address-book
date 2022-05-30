from django.db import models
import uuid
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone


class Address(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = CountryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', related_name='addresses', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (
            'street_name',
            'street_number',
            'zip_code',
            'user'
        )
