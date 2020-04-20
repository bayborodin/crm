
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import DayResult, DataSeries, WeekResult


@receiver(post_save, sender=DataSeries)
def count_day_result(sender, instance, **kwargs):
    metric = instance.metric
    record_date = instance.date

    try:
        day_result = DayResult.objects.get(metric=metric, date=record_date)
    except DayResult.DoesNotExist:
        day_result = DayResult(metric=metric, date=record_date)

    day_result.cnt += 1
    day_result.val += (instance.val // instance.div)
    day_result.save()


@receiver(post_save, sender=DataSeries)
def count_week_result(sender, instance, **kwargs):
    metric = instance.metric

    record_date = instance.date
    year = record_date.year
    week = record_date.isocalendar()[1]

    try:
        week_result = WeekResult.objects.get(metric=metric, year=year, week=week)
    except WeekResult.DoesNotExist:
        week_result = WeekResult(metric=metric, year=year, week=week)

    week_result.cnt += 1
    week_result.val += (instance.val // instance.div)
    week_result.save()
