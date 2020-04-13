from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = 'api'

urlpatterns = [
    # authentication
    path('token-auth/', obtain_auth_token, name='token-auth'),

    # leads
    path('leads/', views.LeadView.as_view(), name='leads'),

    # metrics
    path('metrics/', views.MetricView.as_view(), name='metrics'),
    path('data-sources/', views.DataSourceView.as_view(), name='data_sources'),
    path('data-series/', views.DataSeriesView.as_view(), name='data_series'),
]
