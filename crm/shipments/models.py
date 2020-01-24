from decimal import Decimal

from django.db import models

from accounts.models import LegalEntity
from orders.models import Order


class Shipment(models.Model):
    extid = models.CharField(
        max_length=36,
        db_index=True,
        null=True,
        verbose_name='Внешний код'
    )

    buyer = models.ForeignKey(
        LegalEntity,
        related_name='purchases',
        verbose_name='Покупатель',
        on_delete=models.PROTECT
    )

    consignee = models.ForeignKey(
        LegalEntity,
        related_name='shipments',
        verbose_name='Грузополучатель',
        on_delete=models.PROTECT
    )

    order = models.ForeignKey(
        Order,
        related_name='shipments',
        verbose_name='Заказ',
        on_delete=models.PROTECT
    )

    number = models.CharField(
        max_length=11,
        db_index=True,
        verbose_name='Номер'
    )

    date = models.DateField(verbose_name='Дата')

    total = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Сумма всего',
        default=Decimal(0.00)
    )

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Отгрузка'
        verbose_name_plural = 'Отгрузки'

    def __str__(self):
        return 'Отгрузка'
