# Generated by Django 3.2.3 on 2021-06-29 06:39

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Asset_File', models.FileField(upload_to='covers/')),
                ('Longitude', models.CharField(max_length=255)),
                ('Latitude', models.CharField(max_length=255)),
                ('Multi_Locations', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None), null=True, size=255)),
                ('Expiry_date', models.DateField(null=True)),
                ('Expiry_time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Longitude', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('Latitude', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('Google_maps_link', models.CharField(max_length=200)),
                ('Plus_code', models.CharField(max_length=200)),
                ('Radius', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('Assets', models.ManyToManyField(to='event.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('starting_date', models.DateField(null=True)),
                ('ending_date', models.DateField(null=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('Assets', models.ManyToManyField(to='event.Asset')),
                ('Locations', models.ManyToManyField(to='event.Location')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
