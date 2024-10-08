# Login form

from django import forms
from user.models import User
from django.core import validators
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):

    """
    A form that is used to log in a user. The form requires a username and
    a password.
    """

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Username"),
                "autofocus": "autofocus"
            }
        ),
        min_length=1,
        max_length=42,
        strip=True,
        required=True,
        label=_("Username"),
        validators=[
            validators.RegexValidator(
                regex="^[a-zA-Z0-9_]*$",
                message=(_("Username can only contain letters," +
                           "numbers, and underscores.")),
            )
        ],
    )

    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={"placeholder": _("Password")}),
        min_length=8,
        max_length=100,
        strip=True,
        required=True,
        validators=[
            validators.RegexValidator(
                regex="^[a-zA-Z0-9_]*$",
                message=(_("Password can only contain letters," +
                           "numbers, and underscores.")),
            )
        ],
    )

    class Meta:

        """
        MThe Meta class is used to specify the model and fields that the form
        will use. In this case, the form will use the User model and the
        username and password fields.
        """

        model = User
        fields = ("username", "password")

    def is_valid(self):

        """
        Check if the form is valid, if the user exists and the password
        is correct.
        """

        try:
            # Check if the form is valid
            valid = super(LoginForm, self).is_valid()
            if not valid:
                return False
            # Check if the user exists in the database
            user = User.objects.get(username=self.cleaned_data["username"])
            if not user.check_password(self.cleaned_data["password"]):
                # Check if the password matches the user's password
                self.add_error("password", _("This password is incorrect."))
                return False

        except User.DoesNotExist:
            # If the user does not exist, add an error
            self.add_error("username", _("This user does not exist."))
            return False

        return True
