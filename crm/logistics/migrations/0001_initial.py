# Generated by Django 2.2.4 on 2019-11-15 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DeliveryCompany",
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
                    "name",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Наименование"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=250, verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Транспортная компания",
                "verbose_name_plural": "Транспортные компании",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="DeliveryPriceType",
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
                    "name",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Наименование"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=250, verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип тарифа транспортной компании",
                "verbose_name_plural": "Типы тарифов транспортных компаний",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="DeliveryPrice",
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
                    "departure",
                    models.CharField(
                        db_index=True, max_length=250, verbose_name="Пункт отправления"
                    ),
                ),
                (
                    "destination",
                    models.CharField(
                        db_index=True, max_length=250, verbose_name="Пункт назначения"
                    ),
                ),
                ("weight_from", models.IntegerField(verbose_name="Вес от")),
                ("weight_to", models.IntegerField(verbose_name="Вес до")),
                (
                    "volume_from",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="Объем от"
                    ),
                ),
                (
                    "volume_to",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="Объем до"
                    ),
                ),
                (
                    "base_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Базовый тариф"
                    ),
                ),
                (
                    "expedition_price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Тариф экспедирования",
                    ),
                ),
                (
                    "delivery_company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="prices",
                        to="logistics.DeliveryCompany",
                        verbose_name="Транспортная компания",
                    ),
                ),
                (
                    "price_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="prices",
                        to="logistics.DeliveryPriceType",
                        verbose_name="Тип тарифа",
                    ),
                ),
            ],
        ),
    ]
