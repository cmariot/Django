from django import forms
from tips.models import Tip


class CreateTipForm(forms.Form):

    """
    CreateTipForm is a form for creating a tip.
    """

    content = forms.CharField(
        label="Post your prompt here:",
        min_length=1,
        max_length=1000,
        strip=True,
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "What prompt would you like to share?\n" +
                               "How it has helped you?\n",
                "rows": 3,
                "style": "resize: none;",
                "autofocus": "autofocus"
            }
        ),
    )

    class Meta:

        """
        The Meta class is used to specify the model and fields that the form
        will use. In this case, the form will use the Tip model and the content
        field.
        """

        model = Tip
        fields = ("content",)

    def is_valid(self):

        # Check if the form is valid
        valid = super(CreateTipForm, self).is_valid()
        if not valid:
            self.add_error("content", "Invalid content.")
            return False

        # Check if the content is not empty
        if not self.cleaned_data["content"]:
            self.add_error("content", "Content is required.")
            return False

        # Check if the content is too long
        if len(self.cleaned_data["content"]) > 1000:
            self.add_error("content", "Content is too long.")
            return False

        # Check if the content is too short
        if len(self.cleaned_data["content"]) < 1:
            self.add_error("content", "Content is too short.")
            return False

        return True

    def save(self, user, commit=True):
        # Save the provided tip
        tip = Tip(content=self.cleaned_data["content"], author=user)
        if commit:
            tip.save()
        return tip
