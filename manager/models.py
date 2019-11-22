from django.db import models

class Manager(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name =models.CharField(max_length = 30)
    ssn = models.CharField(max_length = 9)
    salary = models.FloatField()