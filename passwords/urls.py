from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("email-detail/<int:pk>", views.email_detail, name="email_detail"),
    path("password-update/<int:pk>", views.password_update, name="password_update"),
    path("email_add/", views.email_add, name="email_add"),
    path("email-detail/<int:pk>/password_add", views.password_add, name="password_add"),
]
