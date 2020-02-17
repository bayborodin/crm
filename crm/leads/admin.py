from django.contrib import admin

from .models import Lead, LeadChannell, LeadSource


class LeadChannellAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']


class LeadSourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'secret_key']


class LeadAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'channell', 'source']


admin.site.register(LeadChannell, LeadChannellAdmin)
admin.site.register(LeadSource, LeadSourceAdmin)
admin.site.register(Lead, LeadAdmin)
