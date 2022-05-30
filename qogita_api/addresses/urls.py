from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from addresses import views

urlpatterns = [
    path('addresses/', views.AddressList.as_view()),
    path('addresses/<uuid:address_uuid>/', views.AddressDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
