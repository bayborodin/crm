from django.contrib import admin

from .models import Lead, LeadChannel, LeadSource


class LeadChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']


class LeadSourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'secret_key']


class LeadAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'channel', 'source']
    list_filter = (
        'channel',
        'source',
        'delete_mark',
    )


admin.site.register(LeadChannel, LeadChannelAdmin)
admin.site.register(LeadSource, LeadSourceAdmin)
admin.site.register(Lead, LeadAdmin)
