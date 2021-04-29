"""Profile model."""

# Django
from django.db import models

# Utilities
from service_backend.utils.audit_model import AuditModel


class Profile(AuditModel):
    """Profile model.

    A profile holds a user's public data like, picture,
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
