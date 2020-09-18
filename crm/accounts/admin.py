from django.contrib import admin
from .models import AccountType, Account, LegalEntity

from django import forms


# AccountType model admin
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class LegalEntityInline(admin.StackedInline):
    model = LegalEntity
    extra = 0


class AccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['primary_legal_entity'].queryset = LegalEntity.objects.filter(
            account=self.instance
        )


class AccountAdmin(admin.ModelAdmin):
    form = AccountForm
    list_display = [
        'name',
        'get_inn',
        'get_city',
        'account_type',
        'owner',
        'created',
        'updated',
    ]
    list_filter = ['account_type', 'owner']
    search_fields = ['name', 'primary_legal_entity__inn']
    inlines = [LegalEntityInline]

    def get_inn(self, obj):
        if obj.primary_legal_entity:
            return obj.primary_legal_entity.inn

    get_inn.short_description = 'ИНН'

    def get_city(self, obj):
        if obj.primary_legal_entity:
            return obj.primary_legal_entity.city

    get_city.short_description = 'Город'


admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Account, AccountAdmin)
