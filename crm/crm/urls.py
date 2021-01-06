"""Глобальный urls.py."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard/')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('accounts/', include('accounts.urls')),
    path('contracts/', include('contracts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('defections/', include('defections.urls')),
    path('leads', include('leads.urls')),
    path('logistics/', include('logistics.urls')),
    path('users/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'SKAT CRM'
admin.site.site_title = 'SKAT CRM Портал администрирования'
admin.site.index_title = 'Добро пожаловать на портал администрирования SKAT CRM'
