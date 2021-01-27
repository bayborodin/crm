import os
import logging
from decimal import Decimal

from django.db import models
from django.dispatch import receiver

from api.models import Integration
from common.utils import parse_float

DEFAULT_DECIMAL = 0.0
_STRING_FIELD_MAX_LENGTH = 250
_CODE_1C_LENGTH = 12  # noqa: WPS114


logger = logging.getLogger(__name__)


class OfferingGroup(models.Model):
    """Offering group model."""

    extid = models.CharField(
        max_length=36, db_index=True, null=True, verbose_name="Внешний код"
    )

    name = models.CharField(
        max_length=250,
        db_index=True,
        verbose_name="Наименование",
    )

    enabled = models.BooleanField(verbose_name="Активно", default=True)

    @classmethod
    def from_tuple(cls, row):
        offering_group, created = OfferingGroup.objects.get_or_create(
            extid=row[1],
        )
        if created:
            res = "Создана новая товарная группа"
        else:
            res = "Обновлена товарная группа"

        offering_group.name = row[2]
        offering_group.enabled = row[3] == "True"
        offering_group.save()

        return res

    class Meta:
        ordering = ["name"]
        verbose_name = "Товарная группа"
        verbose_name_plural = "Товарные группы"

    def __str__(self):
        return self.name


class Offering(models.Model):
    """Offering model."""

    extid = models.CharField(
        max_length=36, db_index=True, null=True, verbose_name="Внешний код"
    )

    name = models.CharField(max_length=250, db_index=True, verbose_name="Наименование")

    code_1c = models.CharField(max_length=12, db_index=True, verbose_name="Код в 1С")

    short_name = models.CharField(
        max_length=250, db_index=True, verbose_name="Сокращенное наименование"
    )

    group = models.ForeignKey(
        OfferingGroup,
        related_name="offerings",
        verbose_name="Группа",
        on_delete=models.PROTECT,
    )

    url = models.URLField(max_length=250, verbose_name="Карточка в интернет-магазине")

    bulk_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name="Оптовая цена",
        default=Decimal(DEFAULT_DECIMAL),
    )

    retail_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name="Розничная цена",
        default=Decimal(DEFAULT_DECIMAL),
    )

    weight = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        verbose_name="Вес",
        default=Decimal(DEFAULT_DECIMAL),
    )

    volume = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        verbose_name="Объём",
        default=Decimal(DEFAULT_DECIMAL),
    )

    height = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        verbose_name="Высота",
        default=Decimal(DEFAULT_DECIMAL),
    )

    width = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        verbose_name="Ширина",
        default=Decimal(DEFAULT_DECIMAL),
    )

    length = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        verbose_name="Длина",
        default=Decimal(DEFAULT_DECIMAL),
    )

    enabled = models.BooleanField(verbose_name="Активно", default=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def from_tuple(cls, row):
        offerings = Offering.objects.filter(extid=row[1])
        if offerings.exists():
            offering = offerings[0]
            res = "Обновлена позиция номенклатуры"
        else:
            offering = Offering(extid=row[1])
            res = "Создана новая позиция номенклатуры"

        offering_groups = OfferingGroup.objects.filter(extid=row[5])
        if offering_groups.exists():
            offering_group = offering_groups[0]
        else:
            offering_group = OfferingGroup.objects.get(pk=1)

        offering.name = row[3]
        offering.code_1c = row[2]
        offering.short_name = row[4]
        offering.group = offering_group
        offering.url = row[6]
        offering.bulk_price = parse_float(row[7])
        offering.retail_price = parse_float(row[8])
        offering.weight = parse_float(row[9])
        offering.volume = parse_float(row[10])
        offering.height = parse_float(row[11])
        offering.width = parse_float(row[12])
        offering.length = parse_float(row[13])
        offering.enabled = row[14] == "1"

        offering.save()

        return res

    class Meta(object):
        ordering = ["name"]
        verbose_name = "Продукция"
        verbose_name_plural = "Продукция"

    def __str__(self):
        """Return the string represintation of the offering."""
        return self.name


class SparePart(models.Model):
    """Spare part model."""

    name = models.CharField(
        max_length=_STRING_FIELD_MAX_LENGTH,
        db_index=True,
        verbose_name="Наименование",
    )
    mark = models.CharField(
        max_length=_STRING_FIELD_MAX_LENGTH,
        blank=True,
        verbose_name="Маркировка",
    )
    code_1c = models.CharField(  # noqa: WPS114
        max_length=_CODE_1C_LENGTH,
        db_index=True,
        unique=True,
        verbose_name="Код в 1С",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )
    tags = models.TextField(
        blank=True,
        verbose_name="Теги",
    )
    equipment = models.TextField(
        blank=True,
        verbose_name="Совместимое оборудование",
    )
    net_weight = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        verbose_name="Масса нетто, кг.",
        blank=True,
    )
    gross_weight = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        verbose_name="Масса брутто, кг.",
        blank=True,
    )
    length = models.PositiveSmallIntegerField(
        verbose_name="Длина, мм.",
        blank=True,
    )
    width = models.PositiveSmallIntegerField(
        verbose_name="Ширина, мм.",
        blank=True,
    )
    height = models.PositiveSmallIntegerField(
        verbose_name="Высота, мм.",
        blank=True,
    )
    primary_image = models.FileField(
        upload_to="galery/",
        verbose_name="Основной вид",
        blank=True,
    )
    quantity = models.IntegerField(
        verbose_name="Остаток",
        default=0,
    )
    retail_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name="Розничная цена",
        default=Decimal(DEFAULT_DECIMAL),
    )
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def filename(self):
        name = os.path.basename(self.primary_image.name)
        return os.path.splitext(name)[0]

    def __str__(self):
        """Return the string representation of the spare part."""
        return self.name

    class Meta(object):
        ordering = ["name"]
        verbose_name = "Запасная часть"
        verbose_name_plural = "Запасные части"


class SparePartImage(models.Model):
    spare_part = models.ForeignKey(
        SparePart,
        related_name="images",
        verbose_name="Изображение",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255, blank=True)
    file = models.ImageField(upload_to="galery/")
    uploaded_at = models.DateField(auto_now_add=True)


class SparePartIntegration(models.Model):
    spare_part = models.ForeignKey(
        SparePart,
        related_name="integrations",
        verbose_name="Запасная часть",
        on_delete=models.CASCADE,
    )
    integration = models.ForeignKey(
        Integration,
        verbose_name="Интеграция",
        on_delete=models.CASCADE,
    )
    external_code = models.CharField(
        max_length=36, db_index=True, null=True, verbose_name="Внешний код"
    )

    class Meta(object):
        ordering = ("integration",)
        verbose_name = "Интеграция"
        verbose_name_plural = "Интеграции"

    def __str__(self):
        return f"{self.spare_part} ({self.integration.code})"


@receiver(models.signals.post_delete, sender=SparePart)
def auto_delete_file_no_delete(sender, instance, **kwargs):
    """
    Delete files from filesystem
    when corresponding SparePart object is deleted.
    """
    if instance.primary_image:
        if os.path.isfile(instance.primary_image.path):
            os.remove(instance.primary_image.path)


@receiver(models.signals.pre_save, sender=SparePart)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Delete old file from filesystem
    when corresponding SparePart object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = SparePart.objects.get(pk=instance.pk).primary_image
    except SparePart.DoesNotExist:
        return False

    new_file = instance.primary_image

    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    else:
        instance.primary_image = old_file
