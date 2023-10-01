from django.contrib.auth.models import (Permission, Group)
from django.contrib.contenttypes.models import ContentType

from .models import Customer

customer_content_type = ContentType.objects.get_for_model(Customer)
customer_group, created = Group.objects.get_or_create(name='customer')

view_customer_profile_permission, _ = Permission.objects.get_or_create(
    codename='view_customer_profile',
    name='Can view customer profile',
    content_type=customer_content_type,
)

edit_customer_profile_permission, _ = Permission.objects.get_or_create(
    codename='edit_customer_profile',
    name='Can edit customer profile',
    content_type=customer_content_type,
)

customer_group.permissions.add(view_customer_profile_permission, edit_customer_profile_permission)
