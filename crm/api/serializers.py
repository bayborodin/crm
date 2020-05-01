from rest_framework import serializers

from leads.models import Lead
from metrics.models import Metric, DataSource, DataSeries


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
            "channel",
            "source",
            "inn",
            "kpp",
            "company_name",
            "city",
            "address",
            "sale_channels",
            "sale_regions",
            "sale_points",
            "web_address",
            "comment",
            "first_person",
            "first_person_position",
            "bank_account",
            "bank_name",
            "bank_rcbic",
            "bank_corr_account",
            "contact_person",
            "contact_phone",
            "contact_email",
            "pk",
        )

        read_only_fields = ("pk",)


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = (
            "id",
            "name",
        )


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = (
            "id",
            "name",
        )


class DataSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSeries
        fields = ("metric", "dataSource", "registrator", "date", "val", "div")
