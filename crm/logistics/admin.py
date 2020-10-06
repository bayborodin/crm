from django.contrib import admin

from .models import DeliveryCompany, DeliveryPrice, DeliveryPriceType


class DeliveryCompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class DeliveryPriceTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class DeliveryPriceAdmin(admin.ModelAdmin):
    list_display = ['code', 'delivery_company', 'departure', 'destination',
                    'weight_from', 'weight_to', 'volume_from', 'volume_to',
                    'price_type', 'base_price', 'expedition_price']
    list_filter = ['delivery_company', 'departure', 'destination', 'price_type']


admin.site.register(DeliveryCompany, DeliveryCompanyAdmin)
admin.site.register(DeliveryPriceType, DeliveryPriceTypeAdmin)
admin.site.register(DeliveryPrice, DeliveryPriceAdmin)
