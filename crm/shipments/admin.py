from django.contrib import admin

from .models import Shipment


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'number', 'buyer', 'total']
    list_filter = ['date']


admin.site.register(Shipment, ShipmentAdmin)
