# Generated by Django 3.0.2 on 2020-09-21 05:15

from decimal import Decimal

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offerings", "0003_auto_20200114_1302"),
    ]

    operations = [
        migrations.CreateModel(
            name="SparePart",
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
                        db_index=True, max_length=250, verbose_name="Наименование"
                    ),
                ),
                (
                    "code_1c",
                    models.CharField(
                        db_index=True, max_length=12, verbose_name="Код в 1С"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        db_index=True, max_length=250, verbose_name="Описание"
                    ),
                ),
                (
                    "tags",
                    models.CharField(
                        db_index=True, max_length=250, verbose_name="Теги"
                    ),
                ),
                (
                    "equipment",
                    models.CharField(
                        db_index=True,
                        max_length=250,
                        verbose_name="Совместимое оборудование",
                    ),
                ),
                (
                    "net_weight",
                    models.DecimalField(
                        decimal_places=3,
                        default=Decimal("0"),
                        max_digits=7,
                        verbose_name="Масса нетто, кг.",
                    ),
                ),
                (
                    "gross_weight",
                    models.DecimalField(
                        decimal_places=3,
                        default=Decimal("0"),
                        max_digits=7,
                        verbose_name="Масса брутто, кг.",
                    ),
                ),
            ],
            options={
                "verbose_name": "Запасная часть",
                "verbose_name_plural": "Запасные части",
                "ordering": ["name"],
            },
        ),
    ]
