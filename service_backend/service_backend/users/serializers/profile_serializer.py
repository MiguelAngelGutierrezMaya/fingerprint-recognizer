"""User serializer."""

# Django
from django.contrib.auth import authenticate

# Django REST framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin

# Serializers
from service_backend.users.serializers.user_serializer import UserModelSerializer

# Model
from service_backend.users.models import Profile


class ProfileModelSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    """Profile model serializer"""

    user = UserModelSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = Profile
        fields = (
            'id',
            'user'
        )
