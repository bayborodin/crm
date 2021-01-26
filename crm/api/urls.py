from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = "api"

router = routers.DefaultRouter()
router.register(r"parts", views.SparePartViewSet, basename="SparePart")
router.register(r"part-images", views.SparePartImageViewSet, basename="SparePartImage")
router.register(
    r"part-integrations",
    views.SparePartIntegrationViewSet,
    basename="SparePartIntegration",
)

urlpatterns = [
    path("calls/", views.CallView.as_view(), name="calls"),
    path("data-series/", views.DataSeriesView.as_view(), name="data_series"),
    path("data-sources/", views.DataSourceView.as_view(), name="data_sources"),
    path("integrations/", views.IntegrationView.as_view(), name="integrations"),
    path("leads/", views.LeadView.as_view(), name="leads"),
    path("metrics/", views.MetricView.as_view(), name="metrics"),
    path("token-auth/", obtain_auth_token, name="token-auth"),
    path("", include(router.urls)),
]
