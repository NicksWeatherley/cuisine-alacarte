from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    manager = models.ForeignKey('manager.Manager')
    menu = models.ForeignKey('menu')
    # I don't think we need a cook row here. cooks point to restaurants
    # We'll have to add types of customers (vip, blocked etc)
    customers = models.ManyToManyField('customer.Customer') # we might later put this in Customer model instead
