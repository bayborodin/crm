# Generated by Django 2.2.8 on 2020-01-14 02:51

from decimal import Decimal

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offerings", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="offering",
            options={
                "ordering": ["name"],
                "verbose_name": "Продукция",
                "verbose_name_plural": "Продукция",
            },
        ),
        migrations.AlterField(
            model_name="offering",
            name="bulk_price",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0"),
                max_digits=9,
                verbose_name="Оптовая цена",
            ),
        ),
        migrations.AlterField(
            model_name="offering",
            name="retail_price",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0"),
                max_digits=9,
                verbose_name="Розничная цена",
            ),
        ),
    ]
