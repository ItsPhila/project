# Generated by Django 2.2.7 on 2020-02-07 05:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 5, 4, 50, 500438, tzinfo=utc)),
        ),
    ]
