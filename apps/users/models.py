from django.contrib.auth.models import (AbstractUser, Group, Permission)
from django.db import models

class AdminUser(AbstractUser):
    # Your admin-specific fields here

    # Add a unique related_name for the groups field
    groups = models.ManyToManyField(Group, related_name='admin_users')

    # Add a unique related_name for the user_permissions field
    user_permissions = models.ManyToManyField(Permission, related_name='admin_users')

class CustomerUser(AbstractUser):
    # Your customer-specific fields here

    # Add a unique related_name for the groups field
    groups = models.ManyToManyField(Group, related_name='customer_users')

    # Add a unique related_name for the user_permissions field
    user_permissions = models.ManyToManyField(Permission, related_name='customer_users')
