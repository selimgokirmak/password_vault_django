from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Email, Password


class EmailAdmin(admin.ModelAdmin):
    list_display = ["email"]
    ordering = ["-email"]


class PasswordAdmin(admin.ModelAdmin):
    list_display = ["email", "website", "password", "password_old", "username", "extra_info"]
    ordering = ["email"]
    list_filter = ["email"]


admin.site.unregister(Group)
admin.site.register(Email, EmailAdmin)
admin.site.register(Password, PasswordAdmin)