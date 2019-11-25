from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class Salesperson(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=9)
    salary = models.FloatField(
        validators=[MinValueValidator(0.01)],
    )

    restaurant = models.ForeignKey(
        'restaurant.Restaurant',
        null=True,
        on_delete=True,
    )

    # TODO: Add relation to items purchased

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Purchase(models.Model):
    item = models.ForeignKey(
        'item.item',
        null=True,
        on_delete=models.SET_NULL,
    )
    purchaser = models.ForeignKey(
        Salesperson,
        null=True,
        on_delete=models.SET_NULL,
    )
    restaurant = models.ForeignKey(
        'restaurant.Restaurant',
        null = True,
        on_delete = models.SET_NULL,
    )
