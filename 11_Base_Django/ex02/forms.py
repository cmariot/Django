from django import forms


class MyForm(forms.Form):

    """
    MyForm class
    Get the text from the form
    The text must not contain line breaks

    """

    text = forms.CharField(
        label="Nouvelle entrée :",
        required=True,
        widget=forms.TextInput(
            attrs={"autofocus": "autofocus"}
        )
    )

    def clean_text(self):
        """
        clean_text method
        Check if the text contains line breaks
        """
        text = self.cleaned_data["text"]
        if "\n" in text or "\r" in text:
            raise forms.ValidationError(
                "Erreur : le texte ne doit pas contenir de retour à la ligne"
            )
        return text
