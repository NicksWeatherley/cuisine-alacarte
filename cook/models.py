from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from app_user.models import User
# Create your models here.

class Cook(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=9)

#   where they work, will reference restaurants table
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.SET_NULL, null = True)

#   if cook gets warned more than 3 times they get a warning
    warnings = models.PositiveIntegerField(validators = [MaxValueValidator(3)], default = 0)

    # TODO: Set min salary posible
    salary = models.FloatField(validators = [MinValueValidator(0.01)])

    def __str__(self):
        return self.first_name + ' ' + self.last_name



