from django.db.models import fields
from rest_framework import serializers

from leads.models import Lead
from metrics.models import DataSeries, DataSource, Metric
from offerings.models import SparePart


class LeadSerializer(serializers.ModelSerializer):
    """Lead model serializer."""

    class Meta(object):
        model = Lead
        fields = (  # noqa: F811
            'channel',
            'source',
            'inn',
            'kpp',
            'company_name',
            'city',
            'address',
            'sale_channels',
            'sale_regions',
            'sale_points',
            'web_address',
            'comment',
            'first_person',
            'first_person_position',
            'bank_account',
            'bank_name',
            'bank_rcbic',
            'bank_corr_account',
            'contact_person',
            'contact_phone',
            'contact_email',
            'pk',
        )

        read_only_fields = ('pk',)


class MetricSerializer(serializers.ModelSerializer):
    """Metric model serializer."""

    class Meta(object):
        model = Metric
        fields = (
            'id',
            'name',
        )


class DataSourceSerializer(serializers.ModelSerializer):
    """Data source model serializer."""

    class Meta(object):
        model = DataSource
        fields = (
            'id',
            'name',
        )


class DataSeriesSerializer(serializers.ModelSerializer):
    """Data series model serializer."""

    class Meta(object):
        model = DataSeries
        fields = ('metric', 'dataSource', 'registrator', 'date', 'val', 'div')


class SparePartSerializer(serializers.HyperlinkedModelSerializer):
    """Spare part model serializer."""

    class Meta(object):
        model = SparePart
        fields = (  # noqa: F811
            'pk', 'name', 'mark', 'code_1c', 'description', 'tags', 'equipment',
            'net_weight', 'gross_weight', 'length', 'width', 'height',
        )
        read_only_fields = ('pk',)
