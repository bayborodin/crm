# Generated by Django 3.0.2 on 2020-06-23 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20200623_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='phone_code',
            field=models.CharField(max_length=5, null=True, verbose_name='Тел. код'),
        ),
    ]