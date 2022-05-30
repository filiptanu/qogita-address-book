from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from addresses import views

urlpatterns = [
    path('addresses', views.AddressList.as_view()),
    path('addresses/<uuid:pk>', views.AddressDetail.as_view()),
    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
