# Generated by Django 3.0.2 on 2020-04-20 03:21

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0011_auto_20200420_1320"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataseries",
            name="date",
            field=models.DateField(
                blank=True, default=datetime.datetime.now, verbose_name="Дата"
            ),
        ),
    ]
