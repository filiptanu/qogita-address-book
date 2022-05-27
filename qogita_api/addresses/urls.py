from django.urls import path
from addresses import views

urlpatterns = [
    path('addresses/', views.address_list),
    path('addresses/<uuid:address_uuid>/', views.address_detail),
]
