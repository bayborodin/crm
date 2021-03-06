# Generated by Django 3.0.2 on 2021-01-12 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_auto_20210112_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contracts.ContractState', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contracts.ContractType', verbose_name='Тип'),
        ),
    ]
