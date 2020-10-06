# Generated by Django 2.2.8 on 2020-01-24 03:38

from decimal import Decimal

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0009_auto_20200120_1126'),
        ('orders', '0011_orderoffering_extid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extid', models.CharField(db_index=True, max_length=36, null=True, verbose_name='Внешний код')),
                ('number', models.CharField(db_index=True, max_length=11, verbose_name='Номер')),
                ('date', models.DateField(verbose_name='Дата')),
                ('total', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9, verbose_name='Сумма всего')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchases', to='accounts.LegalEntity', verbose_name='Покупатель')),
                ('consignee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shipments', to='accounts.LegalEntity', verbose_name='Грузополучатель')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shipments', to='orders.Order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Отгрузка',
                'verbose_name_plural': 'Отгрузки',
                'ordering': ['date'],
            },
        ),
    ]
