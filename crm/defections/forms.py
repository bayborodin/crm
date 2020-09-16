from django import forms

from .models import Defection
from offerings.models import Offering
from shipments.models import Shipment, ShipmentOffering


class DefectionForm(forms.ModelForm):
    damage_photo = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={'multiple': True, 'disabled': True, }),
        label='Фото повреждения',
        required=False,
    )
    package_photo_outside = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={'multiple': True, 'disabled': True, }),
        label='Фото упаковки (снаружи)',
        required=False,
    )
    package_photo_inside = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={'multiple': True, 'disabled': True, }),
        label='Фото упаковки (изнутри)',
        required=False,
    )

    class Meta:
        model = Defection
        fields = ['shipment', 'offering',
                  'serial_number', 'kind', 'description']
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
        self.fields['shipment'].queryset = Shipment.objects.filter(
            buyer__account=account)
        self.fields['offering'].queryset = Offering.objects.none()

        if 'shipment' in self.data:
            try:
                shipment_id = int(self.data.get('shipment'))
                shipment_offerings = ShipmentOffering.objects.filter(
                    shipment_id=shipment_id).all()
                ids = []
                for shipment_offering in shipment_offerings:
                    ids.append(shipment_offering.offering.id)
                self.fields['offering'].queryset = Offering.objects.filter(
                    id__in=ids).order_by('name')

            except(ValueError, TypeError) as e:
                print(e)
        elif self.instance.pk:
            shipment_offerings = ShipmentOffering.objects.filter(
                shipment=self.instance.shipment).all()
            ids = []
            for shipment_offering in shipment_offerings:
                ids.append(shipment_offering.offering.id)
            self.fields['offering'].queryset = Offering.objects.filter(
                id__in=ids).order_by('name')
