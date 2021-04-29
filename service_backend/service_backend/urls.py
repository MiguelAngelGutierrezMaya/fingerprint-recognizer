"""service URL Configuration"""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf.urls import url


admin.site.site_header = 'API Service Systems'
admin.site.site_title = 'Administration'
admin.site.index_title = 'API Service Systems Administration'
admin.autodiscover()

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # url(r'^api/password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('', include(('service_backend.users.urls', 'users'), namespace='users')),
    # re_path(r'^\.well-known/', include('letsencrypt.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
