from decimal import Decimal

from django.db import models

from accounts.models import LegalEntity
from common.utils import parse_date
from common.utils import parse_float
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

    @classmethod
    def from_tuple(cls, row):
        shipments = Shipment.objects.filter(extid=row[1])
        if shipments.exists():
            shipment = shipments[0]
            res = 'Обновлена отгрузка'
        else:
            shipment = Shipment(extid=row[1])
            res = 'Создана новая отгрузка'

        legal_entities = LegalEntity.objects.filter(extid=row[2])
        if legal_entities.exists():
            shipment.buyer = legal_entities[0]
            shipment.consignee = legal_entities[0]
        else:
            raise ValueError(f'Order has unknown buyer id ({row[2]}).')

        orders = Order.objects.filter(extid=row[3])
        if orders.exists():
            shipment.order = orders[0]
        else:
            raise ValueError(f'Shipment has unknown order id ({row[3]}).')

        shipment.number = row[4]

        date_str = row[5].split()[0]

        shipment.date = parse_date(date_str)

        shipment.total = parse_float(row[6])

        shipment.save()

        return res

    class Meta:
        ordering = ['date']
        verbose_name = 'Отгрузка'
        verbose_name_plural = 'Отгрузки'

    def __str__(self):
        return 'Отгрузка'
