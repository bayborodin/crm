from django.contrib import admin

from leads.models import Lead, LeadChannel, LeadSource


class LeadChannelAdmin(admin.ModelAdmin):
    """The admin class for the LeadChannel model."""

    list_display = ['name', 'created', 'updated']


class LeadSourceAdmin(admin.ModelAdmin):
    """The admin class for the LeadSource model."""

    list_display = ['name', 'secret_key']


class LeadAdmin(admin.ModelAdmin):
    """The admin class for the Lead model."""

    list_display = ['id', 'created', 'channel', 'source']
    list_filter = (
        'channel',
        'source',
        'delete_mark',
    )


admin.site.register(LeadChannel, LeadChannelAdmin)
admin.site.register(LeadSource, LeadSourceAdmin)
admin.site.register(Lead, LeadAdmin)
