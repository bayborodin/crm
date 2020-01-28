from django import forms

from .models import Defection


class DefectionForm(forms.ModelForm):
    class Meta:
        model = Defection
        fields = ['serial_number', 'description']
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'cols': 80,
                    'placeholder': 'Введите описание'
                }
            )
        }
