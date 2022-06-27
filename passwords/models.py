from django.db import models


class Email(models.Model):
    email = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.email


class Password(models.Model):
    email = models.ForeignKey(Email, on_delete=models.PROTECT)
    website = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password_old = models.CharField(max_length=100, null=True, blank=True)
    change_date = models.DateField("date_changed", null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    extra_info = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.website