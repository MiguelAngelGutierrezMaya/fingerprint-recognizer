"""User admin."""

# Django
from django.contrib import admin

# Models
from service_backend.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin."""
    list_display = ('first_name', 'last_name', 'username')
    search_fields = ('first_name', 'last_name', 'username')
    list_filter = ('first_name', 'last_name', 'username')
    readonly_fields = ('password',)
