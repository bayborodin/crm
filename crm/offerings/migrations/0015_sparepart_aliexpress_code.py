# Generated by Django 3.0.2 on 2020-10-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offerings", "0014_auto_20201011_2356"),
    ]

    operations = [
        migrations.AddField(
            model_name="sparepart",
            name="aliexpress_code",
            field=models.CharField(
                blank=True, max_length=250, verbose_name="Код AliExpress"
            ),
        ),
    ]
