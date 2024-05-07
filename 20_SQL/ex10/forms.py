from django import forms
from .models import People


class FormEx10(forms.Form):

    min_release_date = forms.DateField(
        label="Minimum release date",
        required=True,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'placeholder': 'YYYY-MM-DD',
        }),
    )
    max_release_date = forms.DateField(
        label="Maximum release date",
        required=True,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'placeholder': 'YYYY-MM-DD',
        }),
    )
    planet_diameter = forms.IntegerField(
        label="Planet diameter (greater than)",
        required=True,
    )
    character_gender = forms.ChoiceField(
        label="Character gender",
        required=True,
        choices=[],
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(FormEx10, self).__init__(*args, **kwargs)
        self.fields['character_gender'].choices = People.objects.values_list(
            'gender', 'gender'
        ).distinct()
