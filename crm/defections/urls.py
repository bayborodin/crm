from django.urls import path

from . import views

app_name = 'defections'

urlpatterns = [
    path('<str:account_extid>', views.index, name='index'),
    path('<str:account_extid>/new', views.new_defection, name='add'),
    path('ajax/load-offerings', views.load_offerings, name='ajax_load_offerings'),
    path('<str:account_extid>/<int:defection_id>', views.defection, name='defection'),
]
