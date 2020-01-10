# Generated by Django 2.2.4 on 2020-01-10 04:45

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OfferingGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extid', models.CharField(db_index=True, max_length=36, null=True, verbose_name='Внешний код')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='Наименование')),
                ('enabled', models.BooleanField(default=True, verbose_name='Активно')),
            ],
            options={
                'verbose_name': 'Товарная группа',
                'verbose_name_plural': 'Товарные группы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extid', models.CharField(db_index=True, max_length=36, null=True, verbose_name='Внешний код')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='Наименование')),
                ('code_1c', models.CharField(db_index=True, max_length=12, verbose_name='Код в 1С')),
                ('short_name', models.CharField(db_index=True, max_length=250, verbose_name='Сокращенное наименование')),
                ('url', models.URLField(max_length=250, verbose_name='Карточка в интернет-магазине')),
                ('bulk_price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=8, verbose_name='Оптовая цена')),
                ('retail_price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=8, verbose_name='Розничная цена')),
                ('weight', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=6, verbose_name='Вес')),
                ('volume', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=6, verbose_name='Объём')),
                ('height', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=6, verbose_name='Высота')),
                ('width', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=6, verbose_name='Ширина')),
                ('length', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=6, verbose_name='Длина')),
                ('enabled', models.BooleanField(default=True, verbose_name='Активно')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='offerings', to='offerings.OfferingGroup', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Продукция',
                'ordering': ['name'],
            },
        ),
    ]