# Generated by Django 2.2.4 on 2019-12-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191030_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='tsid',
            field=models.CharField(db_index=True, max_length=36, null=True, verbose_name='Код в Terrasoft'),
        ),
        migrations.AlterField(
            model_name='accounttype',
            name='tsid',
            field=models.CharField(db_index=True, max_length=36, verbose_name='Код в Terrasoft'),
        ),
    ]