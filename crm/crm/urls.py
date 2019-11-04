"""Глобальный urls.py."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))
]

admin.site.site_header = "SKAT CRM"
admin.site.site_title = "SKAT CRM Портал администрирования"
admin.site.index_title = "Добро пожаловать на портал администрирования SKAT CRM"
