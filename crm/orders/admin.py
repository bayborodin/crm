from django.contrib import admin

from .models import Order, OrderState


# Order model admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'number_1c', 'customer', 'total_amount', 'state']
    list_filter = ['date', 'customer', 'state']


# OrderState model
class OrderStateAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderState, OrderStateAdmin)
