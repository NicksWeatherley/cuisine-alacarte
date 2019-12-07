from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    manager = models.ForeignKey('manager.Manager', on_delete=models.CASCADE)

    # Rating model is depreciated here, but keeping to not force migrations/db remove
    ratings = models.ManyToManyField('ratings.Rating', blank = True,)
    menu = models.ForeignKey('item.Dish', on_delete=models.CASCADE, null=True)
    #customers = models.ManyToManyField('customer.Customer', blank = True)
    def __str__(self):
        return self.name