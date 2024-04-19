from django import forms


class MyForm(forms.Form):

    title = forms.ChoiceField(
        label="Film title",
        choices=[],
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    def __init__(self, choices):
        super(MyForm, self).__init__()
        self.fields["title"].choices = choices
