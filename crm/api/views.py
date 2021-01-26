from django.db.models import query
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import (
    DataSeriesSerializer,
    DataSourceSerializer,
    IntegrationSerializer,
    LeadSerializer,
    MetricSerializer,
    SparePartImageSerializer,
    SparePartIntegrationSerializer,
    SparePartSerializer,
)
from api.models import Integration
from leads.models import Lead
from metrics.models import DataSeries, DataSource, Metric
from offerings.models import SparePart, SparePartImage, SparePartIntegration


class LeadView(APIView):
    def get(self, request):
        leads = Lead.objects.filter(delete_mark=False)
        serializer = LeadSerializer(leads, many=True)

        context = {"leads": serializer.data}

        return Response(context)

    def post(self, request):
        lead = request.data.get("lead")
        serializer = LeadSerializer(data=lead)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        context = {"success": "Lead  created successfully."}

        return Response(context)


class CallView(APIView):
    def post(self, request):
        print(request.data)

        application_token = request.data["auth[application_token]"]
        if application_token != "latrp9uooafyba3g8vsli25u7udosjnc":
            context = {"error": "unknown application token"}
            return Response(context)

        call_type = int(request.data["data[CALL_TYPE]"])
        if call_type > 1:
            ds = DataSeries()
            ds.metric = Metric.objects.get(name="Звонок")
            ds.dataSource = DataSource.objects.get(name="Bitrix24")
            ds.registrator = request.data["data[CALLER_ID]"]
            ds.val = 1
            ds.save()

        context = {"success": "call created successfully."}
        return Response(context)


class MetricView(APIView):
    def get(self, request):
        metrics = Metric.objects.all()
        serializer = MetricSerializer(metrics, many=True)

        context = {"metrics": serializer.data}

        return Response(context)


class DataSourceView(APIView):
    def get(self, request):
        data_sources = DataSource.objects.all()
        serializer = DataSourceSerializer(data_sources, many=True)

        context = {"data_sources": serializer.data}

        return Response(context)


class DataSeriesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data_series = DataSeries.objects.all()
        serializer = DataSeriesSerializer(data_series, many=True)

        context = {"data_series": serializer.data}

        return Response(context)

    def post(self, request):
        data_series = request.data.get("data_series")
        serializer = DataSeriesSerializer(data=data_series)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        context = {"success": "Data Series  created successfully."}

        return Response(context)


class SparePartViewSet(viewsets.ModelViewSet):
    """Spare Part API endpoint."""

    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SparePartSerializer

    def get_queryset(self):
        queryset = SparePart.objects.all()
        code = self.request.query_params.get("code", None)
        if code is not None:
            queryset = queryset.filter(code_1c=code)
        return queryset


class SparePartImageViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SparePartImageSerializer

    def get_queryset(self):
        queryset = SparePartImage.objects.all()
        spare_part = self.request.query_params.get("part", None)
        if spare_part is not None:
            queryset = queryset.filter(spare_part=spare_part)
        return queryset


class SparePartIntegrationViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (IsAuthenticated,)
    serializer_class = SparePartIntegrationSerializer

    def get_queryset(self):
        queryset = SparePartIntegration.objects.all()

        spare_part = self.request.query_params.get("part", None)
        if spare_part is not None:
            queryset = queryset.filter(spare_part=spare_part)

        integration = self.request.query_params.get("integration", None)
        if integration is not None:
            queryset = queryset.filter(integration=integration)

        return queryset


class IntegrationView(APIView):
    def get(self, request):
        integrations = Integration.objects.all()
        serializer = IntegrationSerializer(integrations, many=True)

        context = {"integrations": serializer.data}

        return Response(context)
