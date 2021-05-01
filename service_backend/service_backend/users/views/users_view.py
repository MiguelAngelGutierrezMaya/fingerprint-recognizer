"""Users views."""

# Django conf
from django.conf import settings

# Vars env
import environ

# Django REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Utils
from service_backend.utils.core import compare_image

env = environ.Env()


class UserAPIView(APIView):
    """User login API view."""

    def get(self, request, *args, **kwargs):
        """Handle HTTP GET request."""
        pass

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        use_sdv = True if request.data['use_sdv'].lower() == 'true' else False
        for key, value in request.FILES.items():
            with open(settings.MEDIA_ROOT + '/tmp/' + value.name, 'wb+') as destination:
                for chunk in request.FILES[key].chunks():
                    destination.write(chunk)
            return Response(compare_image(value.name, use_sdv), status=status.HTTP_201_CREATED)
