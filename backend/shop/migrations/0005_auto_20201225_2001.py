# Generated by Django 3.1.4 on 2020-12-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201225_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
    ]