"""User serializer."""

# Django
from django.contrib.auth import authenticate

# Django REST framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin

# Serializers
from service_backend.roles.serializers.role_serializer import RoleModelSerializer

# Model
from service_backend.users.models import User


class UserModelSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    """User model serializer"""

    role = RoleModelSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
            'document_number',
            'role'
        )
