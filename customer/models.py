from django.db import models
from django.utils import timezone
from app_user.models import User

import datetime


class Customer(models.Model):
    """
    Customer model is used for all customers in the cuisine alcarte project.
    Default behavior is to add a visitor upon checkout with and order that was
    completed.
    """

    # Options for the customer type
    CUSTOMER_TYPES = [
        ("VISITOR", "Visitor"),
        ("REGISTERED", "Registered"),
        ("VIP", "VIP"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    customer_type = models.CharField(
        max_length=11, choices=CUSTOMER_TYPES, default="VISITOR"
    )
    first_name = models.CharField(max_length=20, blank=True, default="")
    last_name = models.CharField(max_length=20, blank=True, default="")
    customer_email = models.CharField(max_length=100, blank=True, default="")
    address = models.CharField(max_length=100, blank=True, default="NOTSET")

    restaurant = models.ForeignKey(
        "restaurant.Restaurant", on_delete=models.SET_NULL, null=True,
    )
    
    def __str__(self):
        if self.customer_type == "VISITOR":
            return str(self.customer_type)

        return self.first_name + " " + self.last_name


class Order(models.Model):
    STATUSES = [
        (1, "New"),
        (2, "Preparing"),
        (3, "Out for Delivery"),
        (4, "Completed"),
        (5, "Cancelled"),
        (6, "Rated")
    ]

    status = models.PositiveIntegerField(choices=STATUSES, default=1)
    created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    dishes = models.ManyToManyField("item.Dish",)

    restaurant = models.ForeignKey(
        "restaurant.Restaurant", on_delete=models.SET_NULL, null=True,
    )

    customer = models.ForeignKey(
        "customer.Customer", on_delete=models.SET_NULL, null=True,
    )

