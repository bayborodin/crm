# Generated by Django 3.0.2 on 2021-01-13 07:28

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_contract_is_virtual'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='credit_limit',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10, verbose_name='Кредит-лимит (руб.)'),
        ),
        migrations.AddField(
            model_name='contract',
            name='grace_period',
            field=models.IntegerField(default=0, verbose_name='Отсрочка платежа, дней'),
        ),
    ]
