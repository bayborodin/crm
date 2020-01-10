from django.contrib import admin

from .models import Offering, OfferingGroup


class OfferingGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'enabled']


class OfferingAdmin(admin.ModelAdmin):
    list_display = ['code_1c', 'name', 'group', 'url', 'bulk_price',
                    'retail_price', 'enabled']
    list_filter = ['group', 'enabled']


admin.site.register(OfferingGroup, OfferingGroupAdmin)
admin.site.register(Offering, OfferingAdmin)
