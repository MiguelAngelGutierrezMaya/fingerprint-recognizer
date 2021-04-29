"""User model."""

# Dependencies
from datetime import datetime

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utils
from service_backend.utils.audit_model import AuditModel


class User(AuditModel, AbstractUser):
    """Users model.

    Extends from Django's AbstractUser, the email is unique and add some extra fields."""

    first_name = models.CharField('Nombres', max_length=50, null=False, blank=False)
    last_name = models.CharField('Apellidos', max_length=80, null=False, blank=False)
    phone_number = models.CharField('Numero', max_length=20, null=False, blank=False)
    address = models.CharField('Direccion', max_length=100, null=False, blank=False)
    document_number = models.CharField('Documento', max_length=15, null=False, blank=False)
    email = models.EmailField('Email address', unique=False)

    # ManyToOne Relations
    #role = models.ForeignKey('roles.Role', default=1, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number', 'address', 'document_number']

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
