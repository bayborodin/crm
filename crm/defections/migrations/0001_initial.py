# Generated by Django 2.2.8 on 2020-01-20 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0009_auto_20200120_1126"),
    ]

    operations = [
        migrations.CreateModel(
            name="Defection",
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
                    "serial_number",
                    models.CharField(
                        max_length=20, null=True, verbose_name="Серийный номер"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Описание брака"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="defections",
                        to="accounts.Account",
                        verbose_name="Контрагент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Акт обнаружения брака",
                "verbose_name_plural": "Акты обнаружения брака",
                "ordering": (["updated", "created"],),
            },
        ),
    ]
