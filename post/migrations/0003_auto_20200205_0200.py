# Generated by Django 2.2.7 on 2020-02-04 23:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200205_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 23, 0, 57, 759746, tzinfo=utc)),
        ),
    ]
