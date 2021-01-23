from django.contrib import admin

from .models import Order, OrderOffering, OrderChannel


class OrderOfferingInline(admin.TabularInline):
    model = OrderOffering
    extra = 0


# Order model admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "date", "order_number", "legal_entity", "total", "channel"]
    list_filter = ["date"]
    inlines = [OrderOfferingInline]


class OrderChannelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderChannel, OrderChannelAdmin)
