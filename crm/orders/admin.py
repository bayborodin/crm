from django.contrib import admin

from .models import Order


# Order model admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'order_number', 'customer', 'total']
    list_filter = ['date', 'customer']


admin.site.register(Order, OrderAdmin)
