from decimal import Decimal

from django.db import models


class OfferingGroup(models.Model):
    extid = models.CharField(max_length=36, db_index=True, null=True,
                             verbose_name='Внешний код')

    name = models.CharField(max_length=250, db_index=True,
                            verbose_name='Наименование')

    enabled = models.BooleanField(verbose_name='Активно', default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Товарная группа'
        verbose_name_plural = 'Товарные группы'

    def __str__(self):
        return self.name


class Offering(models.Model):
    extid = models.CharField(max_length=36, db_index=True, null=True,
                             verbose_name='Внешний код')

    name = models.CharField(max_length=250, db_index=True,
                            verbose_name='Наименование')

    code_1c = models.CharField(
        max_length=12,
        db_index=True,
        verbose_name='Код в 1С'
    )

    short_name = models.CharField(max_length=250, db_index=True,
                                  verbose_name='Сокращенное наименование')

    group = models.ForeignKey(
        OfferingGroup, related_name='offerings',
        verbose_name='Группа',
        on_delete=models.PROTECT
    )

    url = models.URLField(
        max_length=250,
        verbose_name='Карточка в интернет-магазине'
    )

    bulk_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Оптовая цена',
        default=Decimal(0.00)
    )

    retail_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Розничная цена',
        default=Decimal(0.00)
    )

    weight = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        verbose_name='Вес',
        default=Decimal(0.00)
    )

    volume = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        verbose_name='Объём',
        default=Decimal(0.00)
    )

    height = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        verbose_name='Высота',
        default=Decimal(0.00)
    )

    width = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        verbose_name='Ширина',
        default=Decimal(0.00)
    )

    length = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        verbose_name='Длина',
        default=Decimal(0.00)
    )

    enabled = models.BooleanField(verbose_name='Активно', default=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'

    def __str__(self):
        return self.name
