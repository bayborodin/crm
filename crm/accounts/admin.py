from django.contrib import admin
from .models import AccountType, Account, LegalEntity

from django import forms


# AccountType model admin
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


class LegalEntityInline(admin.StackedInline):
    model = LegalEntity
    extra = 0


class AccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields["primary_legal_entity"].queryset = LegalEntity.objects.filter(
            account=self.instance
        )


class AccountAdmin(admin.ModelAdmin):
    form = AccountForm
    list_display = ["name", "account_type", "owner", "created", "updated"]
    list_filter = ["account_type", "owner"]
    inlines = [LegalEntityInline]


admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Account, AccountAdmin)
