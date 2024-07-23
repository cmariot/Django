from django.forms import ModelForm
from tips.models import Tip
from django import forms


class CreateTipForm(ModelForm):

    class Meta:
        model = Tip
        fields = ("content",)

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

    def is_valid(self):
        valid = super(CreateTipForm, self).is_valid()
        if not valid:
            self.add_error("content", "Invalid content.")
            return False

        if not self.cleaned_data["content"]:
            self.add_error("content", "Content is required.")
            return False

        if len(self.cleaned_data["content"]) > 1000:
            self.add_error("content", "Content is too long.")
            return False

        if len(self.cleaned_data["content"]) < 1:
            self.add_error("content", "Content is too short.")
            return False

        return True

    def save(self, user, commit=True):
        tip = Tip(content=self.cleaned_data["content"], author=user)
        if commit:
            tip.save()
        return tip
