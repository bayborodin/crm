from django.contrib import admin

from .models import Contract, ContractState, ContractType


class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "contract_number",
        "account",
        "type",
        "state",
        "owner",
        "created",
        "updated",
    )


class ContractStateAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


admin.site.register(Contract, ContractAdmin)
admin.site.register(ContractState, ContractStateAdmin)
admin.site.register(ContractType, ContractTypeAdmin)
