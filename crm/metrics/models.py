from datetime import datetime

from django.db import models


def current_year():
    return datetime.today().year


class Metric(models.Model):
    '''Измеряемые метрики'''
    name = models.CharField(
        max_length=250,
        db_index=True,
        verbose_name='Наименование')

    class Meta:
        verbose_name = 'Метрика'
        verbose_name_plural = 'Метрики'

    def __str__(self):
        return self.name


class DataSource(models.Model):
    '''Источники данных'''
    name = models.CharField(
        max_length=250,
        db_index=True,
        verbose_name='Наименование')

    class Meta:
        verbose_name = 'Источник данных'
        verbose_name_plural = 'Источники данных'

    def __str__(self):
        return self.name


class DataSeries(models.Model):
    '''Аналитические данные, пеереданные из внешних истоников'''
    metric = models.ForeignKey(
        Metric,
        related_name='series',
        verbose_name='Метрика',
        on_delete=models.PROTECT)
    dataSource = models.ForeignKey(
        DataSource,
        related_name='series',
        verbose_name='Источник',
        on_delete=models.PROTECT,
        null=True)
    registrator = models.CharField(
        max_length=250,
        verbose_name='Регистратор',
        blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата')
    val = models.IntegerField(verbose_name='Значение')
    div = models.IntegerField(default=1, verbose_name='K')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

    def __str__(self):
        return f'{self.metric}-{self.date}-{self.val/self.div}'


class DayResult(models.Model):
    metric = models.ForeignKey(
        Metric,
        related_name='day_results',
        verbose_name='Метрика',
        on_delete=models.PROTECT
    )
    date = models.DateField(verbose_name='Дата')
    cnt = models.IntegerField(verbose_name='Количество записей', default=0)
    val = models.IntegerField(verbose_name='Итог', default=0)

    class Meta:
        ordering = ['-date', 'metric']
        verbose_name = 'Итог за день'
        verbose_name_plural = 'Итоги за день'

    def __str__(self):
        return f'{self.metric}-{self.date}-{self.cnt}-{self.val}'


class WeekResult(models.Model):
    metric = models.ForeignKey(
        Metric,
        related_name='week_results',
        verbose_name='Метрика',
        on_delete=models.PROTECT
    )
    year = models.IntegerField(verbose_name='Год', default=current_year)
    week = models.IntegerField(verbose_name='Неделя')
    cnt = models.IntegerField(verbose_name='Количество записей', default=0)
    val = models.IntegerField(verbose_name='Итог', default=0)

    class Meta:
        ordering = ['-year', '-week', 'metric']
        verbose_name = 'Итог за неделю'
        verbose_name_plural = 'Итоги за неделю'

    def __str__(self):
        return f'{self.metric}-{self.year}-{self.week}-{self.cnt}-{self.val}'
