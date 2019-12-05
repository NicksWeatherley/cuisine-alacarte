from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_cook = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_delivery_person = models.BooleanField(default=False)
    is_sales_person = models.BooleanField(default=False)


