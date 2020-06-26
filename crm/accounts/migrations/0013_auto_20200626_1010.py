# Generated by Django 3.0.2 on 2020-06-26 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_auto_20200623_1623'),
        ('accounts', '0012_auto_20200623_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='legalentity',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='domestic_legal_entities', to='common.City', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nation_legal_entities', to='common.Country', verbose_name='Страна'),
        ),
    ]
