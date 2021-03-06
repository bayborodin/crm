# Generated by Django 3.0.2 on 2020-06-23 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0004_country"),
    ]

    operations = [
        migrations.CreateModel(
            name="State",
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
                ("tsid", models.CharField(blank=True, db_index=True, max_length=36)),
                ("name", models.CharField(max_length=250)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="states",
                        to="common.Country",
                        verbose_name="Страна",
                    ),
                ),
            ],
            options={
                "verbose_name": "Регион",
                "verbose_name_plural": "Регионы",
                "ordering": ["name"],
            },
        ),
    ]
