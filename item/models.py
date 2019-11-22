from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField()
    rating = models.ForeignKey('rating.Ratings', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)