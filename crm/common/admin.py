from django.contrib import admin
from .models import CommunicationType

# CommunicationType model admin


class CommunicationTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'is_phone']
    list_filter = ['is_phone']


admin.site.register(CommunicationType, CommunicationTypeAdmin)
