"""Глобальный urls.py."""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url='users/login/')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('accounts/', include('accounts.urls')),
    path('logistics/', include('logistics.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('defections/', include('defections.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "SKAT CRM"
admin.site.site_title = "SKAT CRM Портал администрирования"
admin.site.index_title = "Добро пожаловать на портал администрирования SKAT CRM"
