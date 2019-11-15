# Generated by Django 2.2.4 on 2019-11-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0005_auto_20191116_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryprice',
            name='base_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Базовый тариф'),
        ),
        migrations.AlterField(
            model_name='deliveryprice',
            name='expedition_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Тариф экспедирования'),
        ),
    ]
