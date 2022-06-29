from django import forms

from .models import Password, Email


class PasswordUpdateForm(forms.ModelForm):
    extra_info = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2}))
    class Meta:
        model = Password
        fields = ["website", "password", "password_old", "username", "extra_info"]


class EmailCreateForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ["email"]


class PasswordCreateForm(forms.ModelForm):
    extra_info = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2}))
    class Meta:
        model = Password
        fields = ["website", "password", "password_old", "username", "extra_info"]

    def save_form(self, request, email):
        obj = Password.objects.create(email=email, website=request["website"], password=request["password"], password_old=request["password_old"], 
        username=request["username"], extra_info=request["extra_info"])
        return obj