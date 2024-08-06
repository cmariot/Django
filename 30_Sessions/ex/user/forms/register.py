from django import forms
from user.models import User
from django.core import validators


class RegisterForm(forms.ModelForm):

    """
    RegisterForm is a form for registering a new user.
    """

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "autofocus": "autofocus",
                "autocomplete": "off"
            }
        ),        min_length=1,
        max_length=42,
        required=True,
        strip=False,
        label="Username",
        validators=[
            validators.RegexValidator(
                regex="^[a-zA-Z0-9_]*$",
                message=("Username can only contain letters, " +
                         "numbers, and underscores."),
            )
        ],
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "autocomplete": "off"
            }
        ),
        min_length=8,
        max_length=100,
        required=True,
        strip=False,
        validators=[
            validators.RegexValidator(
                regex="^[a-zA-Z0-9_]*$",
                message=("Password can only contain letters, " +
                         "numbers, and underscores."),
            )
        ],
    )

    confirmation = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password confirmation",
                "autocomplete": "off"
            }
        ),
        min_length=8,
        max_length=100,
        required=True,
        strip=False,
        validators=[
            validators.RegexValidator(
                regex="^[a-zA-Z0-9_]*$",
                message=("Password can only contain letters, " +
                         "numbers, and underscores."),
            )
        ],
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'confirmation')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def is_valid(self):

        # Check if the form is valid
        valid = super(RegisterForm, self).is_valid()
        if not valid:
            return False

        # Check if the password and the password confirmation match
        password1 = self.cleaned_data["password"]
        password2 = self.cleaned_data["confirmation"]
        if not password1 or password1 != password2:
            error = "Password and password confirmation do not match"
            self.add_error("password", error)
            return False

        # Check if the username is already taken
        if User.objects.filter(
            username=self.cleaned_data["username"]
        ).exists():
            self.add_error("username", "Username already taken")
            return False

        return True
