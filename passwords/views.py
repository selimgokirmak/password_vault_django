from django.shortcuts import render

from .models import Email, Password

def index(request):
    emails = Email.objects.all()

    context = {
        "emails": emails,
    }

    return render(request, "index.html", context)