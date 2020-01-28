from django.urls import path

from . import views

app_name = 'defections'

urlpatterns = [
    path('<str:account_extid>', views.index, name='index'),
    path('<str:account_extid>/new', views.new_defection, name='add'),
]
