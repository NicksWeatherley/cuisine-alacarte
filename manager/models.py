from django.db import models
from app_user.models import User


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=9)
    salary = models.FloatField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
