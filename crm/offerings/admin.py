from django.contrib import admin

from offerings.models import Offering, OfferingGroup, SparePart


class OfferingGroupAdmin(admin.ModelAdmin):
    """Offering group admin."""

    list_display = ['name', 'enabled']


class OfferingAdmin(admin.ModelAdmin):
    """Offering admin."""

    list_display = [
        'code_1c', 'name', 'group', 'bulk_price', 'retail_price', 'enabled',
    ]
    list_filter = ['group', 'enabled']


class SparePartAdmin(admin.ModelAdmin):
    """Spare part admin."""

    list_display = [
        'code_1c', 'name', 'net_weight', 'gross_weight',
    ]
    list_filter = ['code_1c', 'name']


admin.site.register(OfferingGroup, OfferingGroupAdmin)
admin.site.register(Offering, OfferingAdmin)
admin.site.register(SparePart, SparePartAdmin)
