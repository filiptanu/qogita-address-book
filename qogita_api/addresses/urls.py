from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from addresses import views

urlpatterns = [
    path('addresses/', views.address_list),
    path('addresses/<uuid:address_uuid>/', views.address_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
