"""Users views."""

# Django REST Framework
from rest_framework.views import APIView


class UserAPIView(APIView):
    """User login API view."""

    def get(self, request, *args, **kwargs):
        """Handle HTTP GET request."""
        pass

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        pass
