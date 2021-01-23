from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.base import Model
from django.utils.dateparse import parse_date

from accounts.models import LegalEntity
from common.utils import parse_float
from offerings.models import Offering


class OrderChannel(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name="Название")
    description = models.CharField(
        max_length=250, verbose_name="Описание", blank=True, null=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Канал продаж"
        verbose_name_plural = "Каналы продаж"

    def __str__(self):
        return self.name


# Order model
class Order(models.Model):
    extid = models.CharField(
        max_length=36, db_index=True, null=True, verbose_name="Внешний код"
    )
    order_number = models.CharField(max_length=11, db_index=True, verbose_name="Номер")
    date = models.DateField(verbose_name="Дата")
    legal_entity = models.ForeignKey(
        LegalEntity,
        related_name="orders",
        verbose_name="Юридическое лицо",
        on_delete=models.PROTECT,
    )
    total = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name="Сумма всего",
        default=Decimal(0.00),
    )
    channel = models.ForeignKey(
        OrderChannel,
        verbose_name="Канал продаж",
        on_delete=models.PROTECT,
        null=True,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def from_tuple(cls, row):
        orders = Order.objects.filter(extid=row[1])
        if orders.exists():
            order = orders[0]
            res = "Обновлён заказ"
        else:
            order = Order(extid=row[1])
            res = "Создан новый заказ"

        legal_entities = LegalEntity.objects.filter(extid=row[4])
        if legal_entities.exists():
            order.legal_entity = legal_entities[0]
        else:
            raise ValueError(f"Order has unknown client id ({row[4]}).")

        order.order_number = row[3]
        order.date = parse_date(row[2])
        order.total = parse_float(row[5])

        order.save()

        return res

    class Meta:
        ordering = ["date"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ {self.order_number} от {self.date} ({self.legal_entity})"


class OrderOffering(models.Model):
    order = models.ForeignKey(
        Order, related_name="offerings", verbose_name="Товары", on_delete=models.CASCADE
    )
    extid = models.CharField(
        max_length=36, db_index=True, null=True, verbose_name="Внешний код"
    )
    offering = models.ForeignKey(
        Offering, verbose_name="Номенклатура", on_delete=models.PROTECT
    )
    quantity = models.IntegerField(
        verbose_name="Количество", default=0, validators=[MinValueValidator(0)]
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=9,
        decimal_places=2,
        default=Decimal(0.00),
        validators=[MinValueValidator(0.00)],
    )
    amount = models.DecimalField(
        verbose_name="Сумма",
        max_digits=9,
        decimal_places=2,
        default=Decimal(0.00),
        validators=[MinValueValidator(0.00)],
    )

    @classmethod
    def from_tuple(cls, row):
        order_rows = OrderOffering.objects.filter(extid=row[1])
        if order_rows.exists():
            order_row = order_rows[0]
            res = "Updated an order string."
        else:
            order_row = OrderOffering(extid=row[1])
            res = "Created a new order string."

        orders = Order.objects.filter(extid=row[2])
        if not orders.exists():
            raise ValueError(f"Order string has unknown order ID ({row[2]}).")
        order_row.order = orders[0]

        offerings = Offering.objects.filter(extid=row[3])
        if not offerings.exists():
            raise ValueError(f"Order string has unknown offering ID ({row[3]}).")
        order_row.offering = offerings[0]

        order_row.quantity = int(row[4])
        order_row.price = parse_float(row[5])
        order_row.amount = parse_float(row[6])

        order_row.save()

        return res

    class Meta:
        ordering = ["id"]
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def __str__(self):
        return f"{self.offering} {self.amount} руб. ({self.price}x{self.quantity})"
