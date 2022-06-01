from django.urls import path, include
from rest_framework.routers import DefaultRouter
from addresses import views


router = DefaultRouter()
router.register(r'addresses', views.AddressViewSet,basename="addresses")
router.register(r'users', views.UserViewSet,basename="users")

urlpatterns = [
    path('addresses/delete_many/', views.delete_many),
    path('', include(router.urls)),
]
