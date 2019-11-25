from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class DeliveryPerson(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=9)
#   where they work, will reference restaurants table
    restaurant = models.ForeignKey(
        'restaurant.Restaurant',
        null = True,
        on_delete = models.SET_NULL)
#   rating (0 - 5) will reference Rating table/app
    # rating = models.ManyToManyField(
    #     'ratings.Rating', through='restaurant.Restaurant')
#   if cook gets warned more than 3 times they get a warning
    warnings = models.PositiveIntegerField(
        validators=[MaxValueValidator(3)], default=0)
    salary = models.FloatField(validators=[MinValueValidator(0.01)])

    def __str__(self):
        return self.first_name + ' ' + self.last_name
# Create your models here.
