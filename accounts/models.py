from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    profilePic = models.ImageField(upload_to='profilePic/', blank=True)
    # phone = PhoneNumberField(null=True, blank=True, unique=True)
    phone_number = models.CharField(null=True, blank=True, unique=True)

