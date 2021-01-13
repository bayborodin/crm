from django.contrib import admin

from .models import DataSeries, DataSource, DayResult, Metric, WeekResult


class MetricAdmin(admin.ModelAdmin):
    list_display = ["name"]


class DataSourceAdmin(admin.ModelAdmin):
    list_display = ["name"]


class DataSeriesAdmin(admin.ModelAdmin):
    list_display = [
        "metric",
        "dataSource",
        "registrator",
        "date",
        "val",
        "div",
        "created",
    ]
    list_filter = ["metric", "date"]


class DayResultAdmin(admin.ModelAdmin):
    list_display = ["metric", "date", "cnt", "val"]


class WeekResultAdmin(admin.ModelAdmin):
    list_display = ["metric", "year", "week", "cnt", "val"]


admin.site.register(Metric, MetricAdmin)
admin.site.register(DataSeries, DataSeriesAdmin)
admin.site.register(DataSource, DataSourceAdmin)
admin.site.register(DayResult, DayResultAdmin)
admin.site.register(WeekResult, WeekResultAdmin)
