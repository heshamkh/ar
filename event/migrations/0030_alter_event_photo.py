# Generated by Django 3.2.3 on 2021-06-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0029_location_assets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]
