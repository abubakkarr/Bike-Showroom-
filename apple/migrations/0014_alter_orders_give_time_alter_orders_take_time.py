# Generated by Django 5.0.4 on 2024-05-13 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0013_alter_orders_give_time_alter_orders_take_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='give_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 13, 14, 13, 21, 167104)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='take_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 13, 14, 13, 21, 167104)),
        ),
    ]
