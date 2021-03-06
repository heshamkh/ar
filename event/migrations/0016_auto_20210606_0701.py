# Generated by Django 3.2.3 on 2021-06-06 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_alter_event_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='asset',
        ),
        migrations.AddField(
            model_name='asset',
            name='Locations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Asset_Locations', to='event.location'),
        ),
        migrations.AlterField(
            model_name='event',
            name='asset',
            field=models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, related_name='Assets', to='event.asset'),
        ),
    ]
