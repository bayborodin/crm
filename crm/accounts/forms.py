from django import forms

from .models import Account


class AccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Account
        fields = ('account_type', 'name', 'owner', 'primary_legal_entity')
