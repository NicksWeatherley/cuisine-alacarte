from django.db import models

from delivery_person.models import Delivery


class ItemRating(models.Model):
    score = models.FloatField()
    note = models.CharField(
        max_length=120,
        blank=True,
        default="",
        )
    item = models.ForeignKey('item.Item', on_delete=models.SET_NULL, null=True)

class DishRating(models.Model):
    score = models.FloatField()
    note = models.CharField(
        max_length=120,
        blank=True,
        default="",
        )
    item = models.ForeignKey('item.Dish', on_delete=models.SET_NULL, null=True)

class CookRating(models.Model):
    score = models.FloatField()
    note = models.CharField(
        max_length=120,
        blank=True,
        default="",
        )
    cook = models.ForeignKey('cook.Cook', on_delete=models.SET_NULL, null=True)

class DeliveryRating(models.Model):
    score = models.FloatField()
    note = models.CharField(
        max_length=120,
        blank=True,
        default="",
        )
    delivery = models.OneToOneField(Delivery, on_delete=models.SET_NULL, null=True)

class CustomerRating(models.Model):
    score = models.FloatField()
    note = models.CharField(
        max_length=120,
        blank=True,
        default="",
        )
    customer = models.ForeignKey('customer.Customer', on_delete=models.SET_NULL, null=True)
