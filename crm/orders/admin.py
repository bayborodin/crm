from django.contrib import admin

from .models import Order


# Order model admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'number_1c', 'customer', 'total_amount']
    list_filter = ['date', 'customer']


admin.site.register(Order, OrderAdmin)
