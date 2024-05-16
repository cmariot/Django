from django import forms
# from django.conf import settings


class SetLanguageForm(forms.Form):
    lang = forms.ChoiceField(
        choices=[
            ("en-us", "English"),
            ("fr-FR", "French"),
        ],
        label="Select Language",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
