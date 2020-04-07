from django.contrib import admin

from .models import Metric, DataSeries, DataSource, DayResult


class MetricAdmin(admin.ModelAdmin):
    list_display = ['name']


class DataSourceAdmin(admin.ModelAdmin):
    list_display = ['name']


class DataSeriesAdmin(admin.ModelAdmin):
    list_display = ['metric', 'dataSource', 'registrator', 'date', 'val', 'div', 'created']


class DayResultAdmin(admin.ModelAdmin):
    list_display = ['metric', 'date', 'cnt', 'val']


admin.site.register(Metric, MetricAdmin)
admin.site.register(DataSeries, DataSeriesAdmin)
admin.site.register(DataSource, DataSourceAdmin)
admin.site.register(DayResult, DayResultAdmin)
