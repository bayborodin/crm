# Generated by Django 3.0.2 on 2021-01-13 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_contract_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='is_virtual',
            field=models.BooleanField(default=False, verbose_name='Виртуальный'),
            preserve_default=False,
        ),
    ]
