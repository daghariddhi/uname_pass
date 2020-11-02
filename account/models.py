from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10)
    alt_phone = models.CharField(max_length=10)
    designation = models.CharField(max_length=10)
    address = models.TextField()