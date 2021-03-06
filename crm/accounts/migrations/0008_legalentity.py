# Generated by Django 2.2.8 on 2020-01-15 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_auto_20200115_1222"),
    ]

    operations = [
        migrations.CreateModel(
            name="LegalEntity",
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
                    "extid",
                    models.CharField(
                        db_index=True,
                        max_length=36,
                        null=True,
                        verbose_name="Внешний код",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=250, verbose_name="Наименование"
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        db_index=True,
                        max_length=250,
                        verbose_name="Сокращенное наименование",
                    ),
                ),
                (
                    "inn",
                    models.CharField(db_index=True, max_length=12, verbose_name="ИНН"),
                ),
                (
                    "kpp",
                    models.CharField(db_index=True, max_length=9, verbose_name="КПП"),
                ),
                (
                    "code_1c",
                    models.CharField(
                        db_index=True, max_length=12, verbose_name="Код в 1С"
                    ),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="legal_entities",
                        to="accounts.Account",
                        verbose_name="Контрагент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Юридическое лицо",
                "verbose_name_plural": "Юридические лица",
                "ordering": ["name"],
            },
        ),
    ]
