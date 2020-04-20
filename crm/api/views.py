from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from leads.models import Lead
from metrics.models import Metric, DataSource, DataSeries

from .serializers import LeadSerializer
from .serializers import MetricSerializer, DataSourceSerializer, DataSeriesSerializer


class LeadView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)

        context = {"leads": serializer.data}

        return Response(context)

    def post(self, request):
        lead = request.data.get('lead')
        serializer = LeadSerializer(data=lead)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        context = {"success": "Lead  created successfully."}

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
        data_series = request.data.get('data_series')
        serializer = DataSeriesSerializer(data=data_series)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        context = {"success": "Data Series  created successfully."}

        return Response(context)
