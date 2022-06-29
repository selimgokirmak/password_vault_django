from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("email-detail/<int:pk>", views.email_detail, name="email_detail"),
    path("password-update/<int:pk>", views.password_update, name="password_update"),
    # path("update/<int:pk>", views.PasswordUpdateView.as_view(), name="password_update")
]
