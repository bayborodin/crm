# Generated by Django 3.0.2 on 2020-06-23 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='tsid',
            new_name='ext',
        ),
    ]
