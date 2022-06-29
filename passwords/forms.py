from django import forms

from .models import Password


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ["website", "password", "password_old", "change_date", "username", "extra_info"]
