from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = 'api'

urlpatterns = [
    path('leads/', views.LeadView.as_view(), name='leads'),
    path('token-auth/', obtain_auth_token, name='token-auth'),
]
