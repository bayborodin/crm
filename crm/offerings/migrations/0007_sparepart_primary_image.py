# Generated by Django 3.0.2 on 2020-10-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offerings", "0006_auto_20200930_2131"),
    ]

    operations = [
        migrations.AddField(
            model_name="sparepart",
            name="primary_image",
            field=models.FileField(
                null=True, upload_to="galery/", verbose_name="Основное изображение"
            ),
        ),
    ]
