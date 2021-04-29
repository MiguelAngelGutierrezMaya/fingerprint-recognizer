# Django REST framework
from rest_framework import permissions
from rest_framework.authtoken.models import Token

# utils
from service_backend.utils.constants import Constants


def get_user_by_token(request):
    try:
        return Token.objects.get(key=request.headers['Authorization'].split()[1]).user
    except Exception:
        return None


def verify_admin_user(request):
    try:
        user = get_user_by_token(request)
        if user.role.name != Constants.ROLE_ADMIN:
            return False
    except Exception:
        return False
    return True


def verify_key_notification(key):
    return True


class AdminPermision(permissions.BasePermission):
    message = 'Don`t has permission to access,No tienes permiso de acceso'

    def has_permission(self, request, view):
        return verify_admin_user(request)


class PartialPatchPermision(permissions.BasePermission):
    message = 'Don`t has permission to access,No tienes permiso de acceso'

    def has_permission(self, request, view):
        if request.method == 'PATCH':
            return True
        return verify_admin_user(request)


class PartialGetPermision(permissions.BasePermission):
    message = 'Don`t has permission to access,No tienes permiso de acceso'

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return verify_admin_user(request)
