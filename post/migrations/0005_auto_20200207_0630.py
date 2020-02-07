# Generated by Django 2.2.7 on 2020-02-07 03:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200207_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='myimage',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 3, 30, 30, 497430, tzinfo=utc)),
        ),
    ]