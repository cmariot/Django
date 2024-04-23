from django import forms


class UpdateMovie(forms.Form):

    title = forms.ChoiceField(
        label="Film title",
        choices=[],
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    new_opening_crawl = forms.CharField(
        label="Opening crawl",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Enter the opening crawl",
                "style": "resize: none",
                "required": "required"

            }
        )
    )

    def __init__(self, choices):
        super(UpdateMovie, self).__init__()
        self.fields["title"].choices = choices
