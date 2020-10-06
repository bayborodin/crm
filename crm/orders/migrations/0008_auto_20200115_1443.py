# Generated by Django 2.2.8 on 2020-01-15 04:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_legal_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='legal_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='accounts.LegalEntity', verbose_name='Юридическое лицо'),
        ),
    ]
