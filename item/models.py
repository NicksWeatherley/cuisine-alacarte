from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class Item(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )

    restaurant = models.ForeignKey(
        'restaurant.Restaurant', null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=25)
    items = models.ManyToManyField(Item, blank=True)
    price = models.FloatField()

    restaurants = models.ManyToManyField('restaurant.Restaurant')

