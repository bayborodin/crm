# Generated by Django 3.0.2 on 2020-04-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0002_auto_20200407_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Источник данных',
                'verbose_name_plural': 'Источники данных',
            },
        ),
        migrations.AlterModelOptions(
            name='metric',
            options={'verbose_name': 'Метрика', 'verbose_name_plural': 'Метрики'},
        ),
    ]