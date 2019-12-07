from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    manager = models.ForeignKey('manager.Manager', on_delete=models.CASCADE)
    menu = models.ForeignKey('item.Dish', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name