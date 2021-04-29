"""Users URLs"""

# Django
from django.urls import path
from django.conf.urls import url

# Django REST framework
from rest_framework.urlpatterns import format_suffix_patterns

# Views
from service_backend.users.views import (
    UserAPIView
)


urlpatterns = [
    path('api/users/', UserAPIView.as_view(), name='users'),
    # path('api/register/', UserSignUpAPIView.as_view(), name='security_register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
