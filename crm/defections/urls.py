from django.urls import path

from . import views

app_name = 'defections'

urlpatterns = [
    path('', views.index)
]
