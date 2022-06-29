from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from .models import Email, Password
from .forms import PasswordUpdateForm, EmailCreateForm, PasswordCreateForm


def index(request):
    emails = Email.objects.all()
    context = {
        "emails": emails,
    }
    return render(request, "index.html", context)


def email_detail(request, pk):
    passwords = Password.objects.filter(email = pk)
    context = {
        "passwords": passwords,
        "email_id": pk
    }
    return render(request, "passwords/email_detail.html", context)


def password_update(request, pk):
    password_instance = get_object_or_404(Password, pk=pk)

    if request.method == "POST":
        form = PasswordUpdateForm(request.POST, instance=password_instance)

        if form.is_valid():
            form.save()
            return redirect("email_detail", pk=password_instance.email.id)

    else:
        form = PasswordUpdateForm(instance=password_instance)

    context = {
        "form": form,
    }

    return render(request, "passwords/password_update.html", context)


def email_add(request):
    if request.method == "POST":
        form = EmailCreateForm(request.POST)
        form.save()
        return redirect("index")

    else:
        form = EmailCreateForm()

    context = {
        "form": form
    }

    return render(request, "passwords/email_add.html", context)


def password_add(request, pk):
    email = get_object_or_404(Email, pk=pk)

    if request.method == "POST":
        form = PasswordCreateForm(request.POST)
        obj = form.save_form(request.POST, email)
        obj.save()
        return redirect("email_detail", pk=pk)

    else:
        form = PasswordCreateForm()

    context = {
        "form": form,
        "email": email,
    }

    return render(request, "passwords/password_add.html", context)