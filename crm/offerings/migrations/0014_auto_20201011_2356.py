# Generated by Django 3.0.2 on 2020-10-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0013_auto_20201006_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepart',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sparepart',
            name='equipment',
            field=models.TextField(blank=True, verbose_name='Совместимое оборудование'),
        ),
        migrations.AlterField(
            model_name='sparepart',
            name='tags',
            field=models.TextField(blank=True, verbose_name='Теги'),
        ),
    ]