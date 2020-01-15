from decimal import Decimal

from django.db import models
from django.utils.dateparse import parse_date

from accounts.models import LegalEntity
from common.utils import parse_float


# Order model
class Order(models.Model):
    extid = models.CharField(
        max_length=36,
        db_index=True,
        null=True,
        verbose_name='Внешний код'
    )

    order_number = models.CharField(
        max_length=11,
        db_index=True,
        verbose_name='Номер'
    )

    date = models.DateField(verbose_name='Дата')

    legal_entity = models.ForeignKey(
        LegalEntity,
        related_name='orders',
        verbose_name='Юридическое лицо',
        on_delete=models.PROTECT
    )

    total = models.DecimalField(
        max_digits=9, decimal_places=2,
        verbose_name='Сумма всего',
        default=Decimal(0.00)
    )

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def from_tuple(cls, row):
        orders = Order.objects.filter(extid=row[1])
        if orders.exists():
            order = orders[0]
            res = 'Обновлён заказ'
        else:
            order = Order(extid=row[1])
            res = 'Создан новый заказ'

        legal_entities = LegalEntity.objects.filter(extid=row[4])
        if legal_entities.exists():
            order.legal_entity = legal_entities[0]
        else:
            raise ValueError(f'Order has unknown client id ({row[4]}).')

        order.order_number = row[3]
        order.date = parse_date(row[2])
        order.total = parse_float(row[5])

        order.save()

        return res

    class Meta:
        ordering = ['date']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.order_number} от {self.date} ({self.legal_entity})'
