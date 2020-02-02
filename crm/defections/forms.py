from django import forms

from .models import Defection
from offerings.models import Offering
from shipments.models import Shipment


class DefectionForm(forms.ModelForm):
    damage_photo = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'disabled': True}),
        label='Фото повреждения'
    )
    package_photo_outside = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'disabled': True}),
        label='Фото упаковки (снаружи)'
    )
    package_photo_inside = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'disabled': True}),
        label='Фото упаковки (изнутри)'
    )

    class Meta:
        model = Defection
        fields = ['shipment', 'offering', 'serial_number', 'kind', 'description']
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'cols': 80,
                    'placeholder': 'Укажите, чего не хватает в комплекте'
                }
            ),
        }

    def __init__(self, account, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shipment'].queryset = Shipment.objects.filter(buyer__account=account)
        self.fields['offering'].queryset = Offering.objects.none()
