# Generated by Django 3.2.7 on 2021-10-26 22:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0008_bookings_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 22, 5, 58, 560409, tzinfo=utc)),
        ),
    ]
