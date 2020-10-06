from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from accounts.models import LegalEntity
from common.utils import parse_date, parse_float
from offerings.models import Offering
from orders.models import Order


class Shipment(models.Model):
    extid = models.CharField(
        max_length=36, db_index=True, null=True, verbose_name="Внешний код"
    )

    seller = models.ForeignKey(
        LegalEntity,
        related_name="sales",
        verbose_name="Поставщик",
        on_delete=models.PROTECT,
        null=True,
    )

    buyer = models.ForeignKey(
        LegalEntity,
        related_name="purchases",
        verbose_name="Покупатель",
        on_delete=models.PROTECT,
    )

    consignee = models.ForeignKey(
        LegalEntity,
        related_name="shipments",
        verbose_name="Грузополучатель",
        on_delete=models.PROTECT,
    )

    order = models.ForeignKey(
        Order, related_name="shipments", verbose_name="Заказ", on_delete=models.PROTECT,
    )

    number = models.CharField(
        max_length=11, db_index=True, verbose_name="Номер")

    date = models.DateField(verbose_name="Дата")

    total = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name="Сумма всего",
        default=Decimal(0.00),
    )

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def from_tuple(cls, row):
        # Shipment
        shipments = Shipment.objects.filter(extid=row[1])
        if shipments.exists():
            shipment = shipments[0]
            res = "Обновлена отгрузка"
        else:
            shipment = Shipment(extid=row[1])
            res = "Создана новая отгрузка"

        # Legal Entity
        legal_entities = LegalEntity.objects.filter(extid=row[2])
        if legal_entities.exists():
            shipment.buyer = legal_entities[0]
            shipment.consignee = legal_entities[0]
        else:
            raise ValueError(f"Order has unknown buyer id ({row[2]}).")

        # Seller
        if row[4].find("/") >= 0:
            inn, kpp = row[4].split("/")
        else:
            inn = row[4]
            kpp = None
        legal_entities = LegalEntity.objects.filter(inn=inn, kpp=kpp)
        if legal_entities.exists():
            shipment.seller = legal_entities[0]
        else:
            legal_entities = LegalEntity.objects.filter(inn=inn)
            if legal_entities.exists():
                shipment.seller = legal_entities[0]
            else:
                raise ValueError(f"Order has unknown seller INN/KPP ({row[4]})")

        # Order
        orders = Order.objects.filter(extid=row[5])
        if orders.exists():
            shipment.order = orders[0]
        else:
            raise ValueError(f"Shipment has unknown order id ({row[5]}).")

        # Other fields
        shipment.number = row[6]
        date_str = row[7].split()[0]
        shipment.date = parse_date(date_str)
        shipment.total = parse_float(row[8])

        shipment.save()

        return res

    class Meta:
        ordering = ["date"]
        verbose_name = "Отгрузка"
        verbose_name_plural = "Отгрузки"

    def __str__(self):
        return f'Реализация № {self.number} от {self.date.strftime("%d.%m.%Y")}'


class ShipmentOffering(models.Model):
    extid = models.CharField(
        max_length=36, db_index=True, null=True, verbose_name="Внешний код"
    )

    shipment = models.ForeignKey(
        Shipment,
        related_name="offerings",
        verbose_name="Отгрузка",
        on_delete=models.PROTECT,
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
        shipment_offerings = ShipmentOffering.objects.filter(extid=row[1])
        if shipment_offerings.exists():
            shipment_offering = shipment_offerings[0]
            res = "Обновлена строка отгрузки"
        else:
            shipment_offering = ShipmentOffering(extid=row[1])
            res = "Создана новая строка отгрузки"

        shipments = Shipment.objects.filter(extid=row[2])
        if not shipments.exists():
            raise ValueError(
                f"Shipment string has unknown shipment ID ({row[2]}).")
        shipment_offering.shipment = shipments[0]

        offerings = Offering.objects.filter(extid=row[3])
        if not offerings.exists():
            raise ValueError(
                f"Shipment string has unknown offering ID ({row[3]}).")
        shipment_offering.offering = offerings[0]

        shipment_offering.quantity = int(row[4])
        shipment_offering.amount = parse_float(row[5])
        shipment_offering.price = shipment_offering.amount / shipment_offering.quantity

        shipment_offering.save()

        return res

    class Meta:
        ordering = ["id"]
        verbose_name = "Товар в отгрузке"
        verbose_name_plural = "Товары в отгрузке"

    def __str__(self):
        return f"{self.offering} {self.amount} руб. ({self.price}x{self.quantity})"
