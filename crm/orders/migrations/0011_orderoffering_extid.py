# Generated by Django 2.2.8 on 2020-01-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_orderoffering'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderoffering',
            name='extid',
            field=models.CharField(db_index=True, max_length=36, null=True, verbose_name='Внешний код'),
        ),
    ]