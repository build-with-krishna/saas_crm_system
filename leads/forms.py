from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead

        exclude = (
            'company',
            'created_at'
        )