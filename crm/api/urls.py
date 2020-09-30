from os import name
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'parts', views.SparePartViewSet)

urlpatterns = [
    # authentication
    path('token-auth/', obtain_auth_token, name='token-auth'),
    # leads
    path('leads/', views.LeadView.as_view(), name='leads'),
    # metrics
    path('metrics/', views.MetricView.as_view(), name='metrics'),
    path('data-sources/', views.DataSourceView.as_view(), name='data_sources'),
    path('data-series/', views.DataSeriesView.as_view(), name='data_series'),
    path('calls/', views.CallView.as_view(), name='calls'),
    path('', include(router.urls)),
]
