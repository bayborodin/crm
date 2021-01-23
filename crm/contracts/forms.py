from django import forms

from .models import Contract


class ContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    class Meta:
        model = Contract
        fields = (
            "contract_number",
            "account",
            "type",
            "state",
            "is_virtual",
            "credit_limit",
            "grace_period",
        )
