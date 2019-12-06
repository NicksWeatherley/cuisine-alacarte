from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    manager = models.ForeignKey('manager.Manager', on_delete=models.CASCADE)
    # menu = models.ForeignKey('menu', on_delete=models.CASCADE)
    # I don't think we need a cook row here. cooks point to restaurants
    # We'll have to add types of customers (vip, blocked etc)
    #customers = models.ManyToManyField('customer.Visitor') # we might later put this in Customer model instead
    ratings = models.ManyToManyField('ratings.Rating', blank = True)
    menu = models.ForeignKey('item.Dish', on_delete=models.SET_NULL, null = True)
    #customers = models.ManyToManyField('customer.Customer', blank = True)
    def __str__(self):
        return self.name