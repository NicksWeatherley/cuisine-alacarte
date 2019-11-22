from django.db import models

class Rating(models.Model):
    score = models.FloatField()
    resturant = models.ForeignKey('restaurant.Restaurant', on_delete = models.CASCADE)
