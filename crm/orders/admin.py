from django.contrib import admin

from .models import Order, OrderOffering


class OrderOfferingInline(admin.TabularInline):
    model = OrderOffering
    extra = 0


# Order model admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "date", "order_number", "legal_entity", "total"]
    list_filter = ["date"]
    inlines = [OrderOfferingInline]


admin.site.register(Order, OrderAdmin)
