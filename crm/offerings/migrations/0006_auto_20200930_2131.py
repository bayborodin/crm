# Generated by Django 3.0.2 on 2020-09-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0005_auto_20200930_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepart',
            name='description',
            field=models.CharField(max_length=250, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sparepart',
            name='equipment',
            field=models.CharField(max_length=250, null=True, verbose_name='Совместимое оборудование'),
        ),
        migrations.AlterField(
            model_name='sparepart',
            name='tags',
            field=models.CharField(max_length=250, null=True, verbose_name='Теги'),
        ),
    ]