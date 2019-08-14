from django.contrib import admin
from .models import AccountType, Account

# AccountType model admin
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


# Account model admin
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'account_type', 'created', 'updated']
    list_filter = ['account_type']

admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Account, AccountAdmin)