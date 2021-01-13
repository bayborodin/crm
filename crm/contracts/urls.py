"""Определение схемы URL для contracts."""

from django.urls import path

from . import views

app_name = "contracts"

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("<int:contract_id>", views.edit, name="edit"),
]
