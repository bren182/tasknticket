# Generated by Django 2.0.4 on 2018-07-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180516_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='completed_date',
            field=models.DateTimeField(null=True),
        ),
    ]