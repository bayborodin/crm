from django.contrib import admin
from .models import AccountType, Account, LegalEntity


# AccountType model admin
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class LegalEntityInline(admin.StackedInline):
    model = LegalEntity
    extra = 0


class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'account_type', 'owner', 'created', 'updated']
    list_filter = ['account_type']
    inlines = [LegalEntityInline]


admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Account, AccountAdmin)
