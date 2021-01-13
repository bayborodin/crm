# Generated by Django 2.2.8 on 2020-01-15 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_legalentity"),
        ("orders", "0006_auto_20200115_1213"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="legal_entity",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="orders",
                to="accounts.LegalEntity",
                verbose_name="Юридическое лицо",
            ),
        ),
    ]
