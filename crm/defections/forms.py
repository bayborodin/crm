from django import forms

from .models import Defection
from offerings.models import Offering
from shipments.models import Shipment


class DefectionForm(forms.ModelForm):
    class Meta:
        model = Defection
        fields = ['shipment', 'offering', 'serial_number', 'kind', 'description']
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'cols': 80,
                    'placeholder': 'Введите описание'
                }
            )
        }

    def __init__(self, account, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shipment'].queryset = Shipment.objects.filter(buyer__account=account)
        self.fields['offering'].queryset = Offering.objects.none()
