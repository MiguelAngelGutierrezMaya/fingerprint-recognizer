# Django REST Framework
from rest_framework.views import APIView


class RoleAPIView(APIView):
    """Role API view."""

    def get(self, request, *args, **kwargs):
        """Handle HTTP GET request."""
        pass
