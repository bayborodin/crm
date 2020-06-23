# Generated by Django 3.0.2 on 2020-06-23 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_auto_20200623_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationtype',
            name='code',
            field=models.CharField(max_length=6, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='communicationtype',
            name='is_phone',
            field=models.BooleanField(default=False, verbose_name='Для звонков'),
        ),
        migrations.AlterField(
            model_name='communicationtype',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Наименование'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extid', models.CharField(blank=True, db_index=True, max_length=36)),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('phone_code', models.IntegerField(max_length=5, null=True, verbose_name='Тел. код')),
                ('kladr_code', models.CharField(max_length=13, null=True, verbose_name='КЛАДР')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='common.Country', verbose_name='Страна')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subjects', to='common.State', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['name'],
            },
        ),
    ]
