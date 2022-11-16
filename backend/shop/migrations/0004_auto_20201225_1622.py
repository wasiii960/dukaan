# Generated by Django 3.1.4 on 2020-12-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201224_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'pending'), (2, 'accepted'), (3, 'shipped'), (4, 'delivered')], default=1),
        ),
    ]
