from django import forms


class RemoveMovie(forms.Form):

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
        super(RemoveMovie, self).__init__()
        self.fields["title"].choices = choices


