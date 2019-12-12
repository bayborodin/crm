"""Определение схемы URL для accounts."""

from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index)
]