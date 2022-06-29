from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from .models import Email, Password
from .forms import PasswordForm


def index(request):
    emails = Email.objects.all()
    context = {
        "emails": emails,
    }
    return render(request, "index.html", context)


def email_detail(request, pk):
    passwords = Password.objects.filter(email = pk)
    context = {
        "passwords": passwords
    }
    return render(request, "passwords/email_detail.html", context)


def password_update(request, pk):
    password_instance = get_object_or_404(Password, pk=pk)

    if request.method == "POST":
        form = PasswordForm(request.POST, instance=password_instance)

        if form.is_valid():
            form.save()
            return redirect("email_detail", pk=password_instance.email.id)

    else:
        form = PasswordForm(instance=password_instance)

    context = {
        "form": form,
    }

    return render(request, "passwords/password_update.html", context)