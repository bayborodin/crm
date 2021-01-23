from django.contrib import admin

from .models import Integration


class IntegrationAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "description")


admin.site.register(Integration, IntegrationAdmin)
