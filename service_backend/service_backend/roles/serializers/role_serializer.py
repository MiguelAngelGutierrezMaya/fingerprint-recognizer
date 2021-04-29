"""Role serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from service_backend.roles.models import Role


class RoleModelSerializer(serializers.ModelSerializer):
    """Role model serializer."""

    class Meta:
        """Meta class."""
        model = Role
        fields = [
            'id',
            'name',
        ]