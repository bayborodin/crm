from django.contrib import admin

from .models import Shipment, ShipmentOffering


class ShipmentOfferingInline(admin.TabularInline):
    model = ShipmentOffering
    extra = 0


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'number', 'buyer', 'total']
    list_filter = ['date']
    inlines = [ShipmentOfferingInline]


admin.site.register(Shipment, ShipmentAdmin)
