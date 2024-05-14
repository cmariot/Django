from django import forms
from .models import Message


class MessageForm(forms.Form):
    """
    MessageForm is a form for asking a question.
    """

    content = forms.CharField(
        label="Your question:",
        min_length=1,
        max_length=1000,
        strip=True,
        required=True,
    )

    class Meta:
        model = Message
        fields = ["content"]

    def is_valid(self):
        # Check if the form is valid
        valid = super(MessageForm, self).is_valid()
        if not valid:
            return False
        return True

    def save(self, commit=True):
        message = Message(content=self.cleaned_data["content"])
        if commit:
            message.save()
        return message
