"""Определение схемы URL для accounts."""

from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('<int:account_id>', views.detail, name='detail'),
    path('<int:account_id>/edit', views.edit, name='edit'),
]
