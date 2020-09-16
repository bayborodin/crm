from django.db import models

from accounts.models import Account
from offerings.models import Offering
from shipments.models import Shipment


class Defection(models.Model):
    account = models.ForeignKey(
        Account,
        related_name='defections',
        verbose_name='Контрагент',
        on_delete=models.PROTECT,
    )

    shipment = models.ForeignKey(
        Shipment,
        related_name='defections',
        verbose_name='Отгрузка',
        on_delete=models.PROTECT,
        null=True,
    )

    offering = models.ForeignKey(
        Offering,
        related_name='defections',
        verbose_name='Номенклатура',
        on_delete=models.PROTECT,
        null=True,
    )

    serial_number = models.CharField(
        max_length=20,
        null=True,
        verbose_name='Серийный номер',
    )

    SHORTAGE = 'SH'
    TRANSPORTATION_DAMAGE = 'TG'
    OTHER = 'OT'

    KIND_CHOICES = [
        (SHORTAGE, 'Некомплект'),
        (TRANSPORTATION_DAMAGE, 'Транспортный бой'),
        (OTHER, 'Другое'),
    ]

    kind = models.CharField(
        max_length=2,
        choices=KIND_CHOICES,
        default=SHORTAGE,
        verbose_name='Характер брака'
    )

    description = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Описание брака'
    )

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Акт обранужения брака №{self.id} ({self.account})'

    class Meta:
        verbose_name = 'Акт обнаружения брака'
        verbose_name_plural = 'Акты обнаружения брака'


class Photo(models.Model):
    defection = models.ForeignKey(
        Defection,
        related_name='photos',
        verbose_name='Изображение',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255, blank=True)
    file = models.ImageField(upload_to='defections/%Y/%m/%d')
    uploaded_at = models.DateField(auto_now_add=True)
