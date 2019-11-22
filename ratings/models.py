from django.db import models

class Rating(models.model):
    score = models.FloatField()
    resturant = models.Foreig0nKey('restaurant.Restaurant', on_delete = models.CASCADE)
