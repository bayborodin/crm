from decimal import Decimal

from django.db import models
from accounts.models import Account

# Order model


class Order(models.Model):
    extid = models.CharField(max_length=36, db_index=True, null=True,
                             verbose_name='Внешний код')
    number_1c = models.CharField(max_length=12, db_index=True,
                                 verbose_name='Номер в 1С')
    date = models.DateField(verbose_name='Дата')
    customer = models.ForeignKey(Account, related_name='orders',
                                 verbose_name='Клиент',
                                 on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=8, decimal_places=2,
                                 verbose_name='Стоимость без доставки',
                                 default=Decimal(0.00))
    delivery_amount = models.DecimalField(max_digits=8, decimal_places=2,
                                          verbose_name='Стоимость доставки',
                                          default=Decimal(0.00))
    total_amount = models.DecimalField(max_digits=8, decimal_places=2,
                                       verbose_name='Стоимость с доставкой',
                                       default=Decimal(0.00))
    total_weight = models.DecimalField(max_digits=6, decimal_places=2,
                                       verbose_name='Вес, всего',
                                       default=Decimal(0.00))
    total_volume = models.DecimalField(max_digits=6, decimal_places=2,
                                       verbose_name='Объем, всего',
                                       default=Decimal(0.00))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.number_1c} от {self.date} ({self.customer})'
