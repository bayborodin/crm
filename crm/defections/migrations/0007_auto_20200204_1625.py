# Generated by Django 3.0.2 on 2020-02-04 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('defections', '0006_auto_20200129_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='defection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='defections.Defection', verbose_name='Изображение'),
        ),
    ]
