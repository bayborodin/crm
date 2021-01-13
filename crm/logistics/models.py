from django.db import models

from common.utils import parse_float

# Delivery company model


class DeliveryCompany(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Наименование")
    description = models.CharField(max_length=250, verbose_name="Описание", blank=True)

    class Meta(object):
        ordering = ["name"]
        verbose_name = "Транспортная компания"
        verbose_name_plural = "Транспортные компании"

    def __str__(self):
        return self.name


class DeliveryPriceType(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Наименование")
    description = models.CharField(max_length=250, verbose_name="Описание", blank=True)

    class Meta(object):
        ordering = ["name"]
        verbose_name = "Тип тарифа транспортной компании"
        verbose_name_plural = "Типы тарифов транспортных компаний"

    def __str__(self):
        return self.name


class DeliveryPrice(models.Model):
    code = models.CharField(max_length=6, db_index=True, verbose_name="Код")
    delivery_company = models.ForeignKey(
        DeliveryCompany,
        related_name="prices",
        verbose_name="Транспортная компания",
        on_delete=models.PROTECT,
        null=True,
    )
    departure = models.CharField(
        max_length=250, db_index=True, verbose_name="Пункт отправления"
    )
    destination = models.CharField(
        max_length=250, db_index=True, verbose_name="Пункт назначения"
    )
    weight_from = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="Вес от"
    )
    weight_to = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="Вес до"
    )
    volume_from = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="Объем от"
    )
    volume_to = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="Объем до"
    )
    price_type = models.ForeignKey(
        DeliveryPriceType,
        related_name="prices",
        verbose_name="Тип тарифа",
        on_delete=models.PROTECT,
        null=True,
    )
    base_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="Базовый тариф"
    )
    expedition_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Тариф экспедирования",
    )

    @classmethod
    def get_float(cls, numstr):
        return numstr

    @classmethod
    def from_tuple(cls, row):
        delivery_price, created = DeliveryPrice.objects.get_or_create(code=row[1])
        if created:
            res = "Создан новый Тариф транспортной компании"
        else:
            res = "Обновлен Тариф транспортной компании"

        delivery_company, _ = DeliveryCompany.objects.get_or_create(name=row[2])
        delivery_company.save()
        price_type, _ = DeliveryPriceType.objects.get_or_create(name=row[11])
        price_type.save()

        delivery_price.code = row[1]
        delivery_price.delivery_company = delivery_company
        delivery_price.departure = row[3]
        delivery_price.destination = row[4]
        delivery_price.weight_from = parse_float(row[5])
        delivery_price.weight_to = parse_float(row[6])
        delivery_price.volume_from = parse_float(row[7])
        delivery_price.volume_to = parse_float(row[8])
        delivery_price.base_price = parse_float(row[9])
        delivery_price.expedition_price = parse_float(row[10])
        delivery_price.price_type = price_type

        delivery_price.save()

        return res

    class Meta(object):
        ordering = [
            "delivery_company",
            "departure",
            "destination",
            "price_type",
            "weight_from",
            "weight_to",
            "volume_from",
            "volume_to",
        ]
        verbose_name = "Тариф транспортной компании"
        verbose_name_plural = "Тарифы транспортных компаний"

    def __str__(self):
        return f"{self.delivery_company} ({self.departure} - {self.destination})"
