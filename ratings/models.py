from django.db import models


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
    item = models.ForeignKey('cook.Cook', on_delete=models.SET_NULL, null=True)

class DeliveryRating(models.Model):
    score = models.FloatField()
    note = models.CharField(
        max_length=120,
        blank=True,
        default="",
        )
    item = models.ForeignKey('delivery_person.Delivery', on_delete=models.SET_NULL, null=True)

class CustomerRating(models.Model):
    score = models.FloatField()
    note = models.CharField(
        max_length=120,
        blank=True,
        default="",
        )
    item = models.ForeignKey('customer.Customer', on_delete=models.SET_NULL, null=True)
