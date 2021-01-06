from django.db import models

from accounts.models import Account


class Contract(models.Model):
    contract_number = models.CharField(
        max_length=10,
        db_index=True,
        verbose_name='Номер',
        null=True,
        blank=True,
    )
    account = models.ForeignKey(
        Account,
        related_name='contracts',
        verbose_name='Контрагент',
        on_delete=models.PROTECT
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created', 'updated')
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

    def __str__(self):
        return f'Договор №{self.contract_number} ({self.account})'
