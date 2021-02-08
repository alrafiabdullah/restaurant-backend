# Generated by Django 3.1.5 on 2021-02-07 13:43

import accounts.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210207_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='duration',
            field=models.DurationField(choices=[(datetime.timedelta(days=1), '1 day'), (datetime.timedelta(days=3), '3 days'), (datetime.timedelta(days=5), '5 days'), (datetime.timedelta(days=7), '7 days'), (datetime.timedelta(days=15), '15 days'), (datetime.timedelta(days=30), '30 days')], default=datetime.timedelta(days=1)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='name',
            field=models.CharField(default=accounts.models.random_string, max_length=100, unique=True),
        ),
    ]
