# Generated by Django 3.1.5 on 2021-02-07 14:24

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210207_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='number',
            field=models.CharField(default=accounts.models.order_number, max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='size',
            field=models.PositiveIntegerField(choices=[(6, 6), (8, 8), (12, 12), (0, 0)], default=0, null=True),
        ),
    ]
