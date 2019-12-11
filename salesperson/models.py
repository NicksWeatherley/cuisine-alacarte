from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from app_user.models import User


class Salesperson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=9)

    salary = models.FloatField(
        validators=[MinValueValidator(0.01)],
    )
    
    commission = models.FloatField(
        validators=[MinValueValidator(0.01), MaxValueValidator(0.70),],
        default = 0.10
    )

    restaurant = models.ForeignKey(
        'restaurant.Restaurant',
        null=True,
        on_delete=True,
    )

    warnings = models.PositiveIntegerField(validators = [MaxValueValidator(3)], default = 0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Purchase(models.Model):
    total_cost = models.FloatField(
        validators=[MinValueValidator(0.01)],
        default = 0.01,
    )

    quantity = models.IntegerField(
        validators=[MinValueValidator(1)],
        default = 1,
    )

    item = models.ForeignKey(
        'item.item',
        null=True,
        on_delete=models.SET_NULL,
    )

    purchaser = models.ForeignKey(
        Salesperson,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    restaurant = models.ForeignKey(
        'restaurant.Restaurant',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return '%s' % self.item.name