# Generated by Django 2.0.4 on 2018-05-16 10:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180516_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 10, 21, 46, 132817, tzinfo=utc)),
        ),
    ]
