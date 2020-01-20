from django.db import models

from accounts.models import Account


class Defection(models.Model):
    account = models.ForeignKey(
        Account,
        related_name='defections',
        verbose_name='Контрагент',
        on_delete=models.PROTECT
    )

    serial_number = models.CharField(
        max_length=20,
        null=True,
        verbose_name='Серийный номер'
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
