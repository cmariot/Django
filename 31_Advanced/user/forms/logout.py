# Logout form

from django import forms
from django.contrib.auth import logout as auth_logout


class LogoutForm(forms.Form):
    def logout(self, request):
        auth_logout(request)
        return request
