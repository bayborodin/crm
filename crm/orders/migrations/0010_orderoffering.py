# Generated by Django 2.2.8 on 2020-01-17 11:32

from decimal import Decimal

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offerings", "0003_auto_20200114_1302"),
        ("orders", "0009_remove_order_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderOffering",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Количество",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0"),
                        max_digits=9,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                        verbose_name="Цена",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0"),
                        max_digits=9,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                        verbose_name="Сумма",
                    ),
                ),
                (
                    "offering",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="offerings.Offering",
                        verbose_name="Номенклатура",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="offerings",
                        to="orders.Order",
                        verbose_name="Товары",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар в заказе",
                "verbose_name_plural": "Товары в заказе",
                "ordering": ["id"],
            },
        ),
    ]
