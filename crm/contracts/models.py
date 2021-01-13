from django.contrib.auth.models import User
from django.db import models

from accounts.models import Account


class ContractType(models.Model):
    """Supply contract type."""

    name = models.CharField(max_length=50, verbose_name="Название")
    extid = models.CharField(
        max_length=36, db_index=True, verbose_name="Внешний код", blank=True, null=True
    )
    description = models.CharField(
        max_length=250, verbose_name="Описание", blank=True, null=True
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Тип договора"
        verbose_name_plural = "Типы договоров"

    def __str__(self):
        return self.name


class ContractState(models.Model):
    """Supply contract state."""

    name = models.CharField(max_length=50, verbose_name="Название")
    extid = models.CharField(
        max_length=36, db_index=True, verbose_name="Внешний код", blank=True, null=True
    )
    description = models.CharField(
        max_length=250, verbose_name="Описание", blank=True, null=True
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Статус договора"
        verbose_name_plural = "Статусы договоров"

    def __str__(self):
        return self.name


class Contract(models.Model):
    """Supply contract."""

    contract_number = models.CharField(
        max_length=10,
        db_index=True,
        verbose_name="Номер",
        null=True,
        blank=True,
    )
    account = models.ForeignKey(
        Account,
        related_name="contracts",
        verbose_name="Контрагент",
        on_delete=models.PROTECT,
    )
    type = models.ForeignKey(ContractType, verbose_name="Тип", on_delete=models.PROTECT)
    state = models.ForeignKey(
        ContractState, verbose_name="Статус", on_delete=models.PROTECT
    )
    owner = models.ForeignKey(
        User, verbose_name="Ответственный", on_delete=models.PROTECT, null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("created", "updated")
        verbose_name = "Договор"
        verbose_name_plural = "Договоры"

    def __str__(self):
        return f"Договор №{self.contract_number} ({self.account})"
