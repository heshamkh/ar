from django.db import models
import uuid # new
# from django.contrib.auth.models import User


# class Events(models.Model):
#     id = models.UUIDField(
#         primary_key=True,
#         # db_index=True,  # new
#         default=uuid.uuid4,
#         editable=False)
#     Name = models.CharField(max_length=200)
#     Photo = models.ImageField(upload_to='covers/', blank=True)
#     Locations = models.CharField(max_length=200)
#     start_date = models.DateField(null=True)
#     end_date = models.DateField(null=True)
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='Events',
#     )
#
#     def __str__(self):
#         return self.Name

# def get_absolute_url(self):
#     return reverse('book_detail', args=[str(self.id)])


class Assets(models.Model):
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
        ASSETS_TYPE = [
            ("IOS", 'IOS'),
            ("ANDROID", 'Android'),
        ]
        ASSETS_TYPE = models.CharField(
            max_length=8,
            choices=ASSETS_TYPE,
            default="IOS",
        )

        def __str__(self):
            return self.code


# class Locations(models.Model):
#             id = models.UUIDField(
#                 primary_key=True,
#                 # db_index=True,  # new
#                 default=uuid.uuid4,
#                 editable=False)
#             Name = models.CharField(max_length=200)
#             Longitude = models.CharField(max_length=200)
#             Latitude = models.CharField(max_length=200)
#             Google_maps_link = models.CharField(max_length=200)
#             Plus_code = models.CharField(max_length=200)
#             assets = models.ForeignKey(
#                 Assets,
#                 on_delete=models.CASCADE,
#                 related_name='Events',
#             )
#
#             def __str__(self):
#                 return self.Name
