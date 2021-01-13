# Generated by Django 3.0.2 on 2020-10-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offerings", "0011_sparepartimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sparepart",
            name="code_1c",
            field=models.CharField(
                db_index=True, max_length=12, unique=True, verbose_name="Код в 1С"
            ),
        ),
    ]
