# Generated by Django 3.0.2 on 2020-04-07 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0006_auto_20200407_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('cnt', models.IntegerField(default=0, verbose_name='Количество записей')),
                ('val', models.IntegerField(default=0, verbose_name='Итог')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='day_results', to='metrics.Metric', verbose_name='Метрика')),
            ],
            options={
                'verbose_name': 'Итог за день',
                'verbose_name_plural': 'Итоги за день',
                'ordering': ['-date', 'metric'],
            },
        ),
    ]
