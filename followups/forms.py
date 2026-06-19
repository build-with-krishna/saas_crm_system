from django import forms
from .models import FollowUp


class FollowUpForm(forms.ModelForm):

    class Meta:

        model = FollowUp

        exclude = (
            'company',
            'created_at'
        )