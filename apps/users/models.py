from django.contrib.auth.models import (AbstractUser)
from django.db import models


class User(AbstractUser):
    pass


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
