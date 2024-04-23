from django import forms
from .models import People


class FormEx10(forms.Form):

    min_release_date = forms.DateField(
        label="Minimum release date",
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'placeholder': 'YYYY-MM-DD',
        }),
    )
    max_release_date = forms.DateField(
        label="Maximum release date",
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'placeholder': 'YYYY-MM-DD',
        }),
    )
    planet_diameter = forms.IntegerField(
        label="Planet diameter (greater than)",
        required=False,
    )
    character_gender = forms.ModelChoiceField(
        label="Character gender",
        queryset=People.objects.distinct('gender'),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
