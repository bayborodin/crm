from django.contrib import admin

from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_number', 'account', 'created', 'updated')


admin.site.register(Contract, ContractAdmin)
