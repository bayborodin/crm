# Generated by Django 3.0.2 on 2020-01-29 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0003_auto_20200114_1302'),
        ('defections', '0005_defection_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='defection',
            name='offering',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='defections', to='offerings.Offering', verbose_name='Номенклатура'),
        ),
        migrations.AlterField(
            model_name='defection',
            name='kind',
            field=models.CharField(choices=[('SH', 'Некомплект'), ('TG', 'Транспортный бой'), ('OT', 'Другое')], default='SH', max_length=2, verbose_name='Характер брака'),
        ),
    ]
