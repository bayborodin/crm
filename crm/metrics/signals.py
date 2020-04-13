from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import DataSeries, DayResult


@receiver(post_save, sender=DataSeries)
def count_day_result(sender, instance, **kwargs):
    metric = instance.metric
    today = datetime.today().date()

    try:
        day_result = DayResult.objects.get(metric=metric, date=today)
    except DayResult.DoesNotExist:
        day_result = DayResult(metric=metric, date=today)

    day_result.cnt += 1
    day_result.val += (instance.val // instance.div)
    day_result.save()
