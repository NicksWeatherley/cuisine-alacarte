from django.db import models

class Manager(models.model):
    first_name = models.CharField(max_lenght = 20)
    last_name =models.CharField(max_lenght = 30)
    SSN = models.CharField(max_lenght = 9)
    resturant = models.Foreig0nKey('restaurant.Restaurant', on_delete = models.CASCADE)
    salary = models.FloatField()