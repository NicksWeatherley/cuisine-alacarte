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
    ratings = models.ForeignKey('ratings.Rating', on_delete = models.CASCADE, blank = True, null  = True)
    customers = models.ForeignKey('customer.Customer', on_delete = models.CASCADE, blank = True, null  = True)

    def __str__(self):
        return self.name
