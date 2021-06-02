from django.db import models
import uuid
from django.contrib.auth.models import User


class Asset(models.Model):
            id = models.UUIDField(
                primary_key=True,
                # db_index=True,  # new
                default=uuid.uuid4,
                editable=False)
            code = models.CharField(max_length=400)
            featured_image = models.ImageField(upload_to='covers/', blank=True)
            Latitude = models.CharField(max_length=200)
            Google_maps_link = models.CharField(max_length=200)
            Plus_code = models.CharField(max_length=200)
            ASSETS_TYPE = [("IOS", 'IOS'),("ANDROID", 'Android'),]
            ASSETS_TYPE = models.CharField(
                max_length=8,
                choices=ASSETS_TYPE,
                default="IOS",
                )
            Expiry_date = models.DateField(null=True)
            Expiry_time = models.TimeField(null=True)

            def __str__(self):
                return self.code


class Location(models.Model):
            id = models.UUIDField(
                primary_key=True,
                # db_index=True,  # new
                default=uuid.uuid4,
                editable=False)
            Name = models.CharField(max_length=200)
            Longitude = models.CharField(max_length=200)
            Latitude = models.CharField(max_length=200)
            Google_maps_link = models.CharField(max_length=200)
            Plus_code = models.CharField(max_length=200)
            asset = models.ForeignKey(
                        Asset,
                        on_delete=models.CASCADE,
                        related_name='Asset',
               )

            def __str__(self):
                return self.Name


class Event(models.Model):
            id = models.UUIDField(
                 primary_key=True,
                 # db_index=True,  # new
                 default=uuid.uuid4,
                 editable=False)
            Name = models.CharField(max_length=200)
            Photo = models.ImageField(upload_to='covers/', blank=True)
            Locations = models.CharField(max_length=200)
            starting_date = models.DateField(null=True)
            ending_date = models.DateField(null=True)
            user = models.ForeignKey(
                 User,
                 on_delete=models.CASCADE,
                 related_name='Events',
             )

            def __str__(self):
                return self.Name
