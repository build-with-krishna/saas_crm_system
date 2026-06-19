from django import forms
from .models import Deal


class DealForm(forms.ModelForm):

    class Meta:

        model = Deal

        exclude = (
            'company',
            'created_at'
        )