# Generated by Django 3.2.3 on 2021-06-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0023_auto_20210606_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Assets',
            field=models.ManyToManyField(to='event.Asset'),
        ),
    ]
